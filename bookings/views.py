import stripe
from os import getenv
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Booking
from tours.models import Tour
from reviews.models import Review

stripe.api_key = getenv('STRIPE_KEY')

# Create your views here.
@login_required
def bookings(request):
    current_user = request.user
    bookings = current_user.bookings.all()

    return render(
        request,
        "bookings/bookings.html",
        {"current_page": "bookings", "bookings": bookings},
    )


@login_required
def single_booking(request, booking_id):
    current_user = request.user
    booking = get_object_or_404(Booking, pk=booking_id, user=current_user)
    tour = booking.tour
    review = Review.objects.filter(tour=tour, user=current_user).first()

    return render(
        request, "bookings/booking.html", {"booking": booking, "review": review}
    )


@login_required
def make_booking(request, slug):
    if request.method == "POST":
        tour = Tour.objects.filter(slug=slug).first()
        num_of_participant = int(request.POST.get("ppl"))

        if num_of_participant > tour.num_of_spots_left:
            messages.error(
                request,
                f"The number of spots left on the tour is {tour.num_of_spots_left}. Please change the number of participants.",
            )
            context = {"tour": tour, "ppl": num_of_participant}

        else:
            path = reverse("confirm_booking", args=[slug])
            request.session["no_of_participants"] = num_of_participant
            return redirect(path)

    else:
        tour = get_object_or_404(Tour, slug=slug)
        context = {"tour": tour, "ppl": 1}

        if tour.num_of_spots_left == 0:
            messages.error(
                request,
                "The tour is fully booked. Please choose another tour. Sorry for the incovenience caused.",
            )
            path = reverse("tour", args=[slug])
            return redirect(path)

    return render(request, "bookings/new_booking.html", context)


@login_required
def confirm_booking(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    num_of_participants = request.session.get("no_of_participants")
    price = tour.price * num_of_participants
    success_url = request.build_absolute_uri(reverse("booking_success", args=[slug]))
    cancel_url = request.build_absolute_uri(reverse("confirm_booking", args=[slug]))

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "myr",
                        "unit_amount": int(tour.price * 100),
                        "product_data": {"name": tour.name},
                    },
                    "quantity": num_of_participants,
                }
            ],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )

        return render(
            request,
            "bookings/confirm_booking.html",
            {
                "tour": tour,
                "participants": num_of_participants,
                "price": price,
                "checkout_session_id": checkout_session.id,
            },
        )

    except Exception:
        messages.error(
            request,
            "An error just occurred while loading the page. Please refresh the page.",
        )

        return render(
            request,
            "bookings/confirm_booking.html",
            {
                "tour": tour,
                "participants": num_of_participants,
                "price": price,
            },
        )


@login_required
def checkout_success(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    num_of_participants = request.session.get("no_of_participants")
    price = tour.price * num_of_participants
    current_user = request.user

    booking = Booking(
        tour=tour, user=current_user, num_of_people=num_of_participants, price=price
    )
    booking.save()

    tour.num_of_spots_left -= num_of_participants
    tour.save()

    request.session["no_of_participants"] = 0

    messages.success(request, f"Booking for {tour.name} made successfully!")

    return render(
        request,
        "bookings/booking_success.html",
        {
            "tour": tour,
            "price": price,
            "participants": num_of_participants,
            "booking": booking,
        },
    )


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == "POST":
        tour = booking.tour
        num_of_participants = booking.num_of_people
        booking.delete()

        tour.num_of_spots_left += num_of_participants
        tour.save()

        messages.success(request, f"Booking had been cancelled successfully.")

        return redirect(reverse("bookings"))

    return render(request, "bookings/delete_booking.html", {"booking": booking})
