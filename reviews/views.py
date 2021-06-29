from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from tours.models import Tour
from .models import Review

# Create your views here.
def reviews(request, slug):
	tour = get_object_or_404(Tour, slug=slug)
	reviews = tour.reviews.all()

	return render(
		request,
		"reviews/reviews.html",
		{"tour": tour, "reviews": reviews, "numbers": [1, 2, 3, 4, 5]},
	)


@login_required
def add_review(request, slug):
	tour = get_object_or_404(Tour, slug=slug)
	review = tour.reviews.filter(user=request.user).first()
	
	if review:
		messages.error(request, "A review is already added for this tour.")
		return redirect(reverse("bookings"))

	elif request.method == "POST":
		form = ReviewForm(request.POST)

		if form.is_valid():
			form_data = form.save(commit=False)
			form_data.user = request.user
			form_data.tour = tour
			form_data.save()

			tour.update_rating()

			messages.success(request, "The review was added successfully!")

			return redirect(reverse("bookings"))
	else:
		form = ReviewForm()

	return render(request, "reviews/new_review.html", {"form": form, "tour": tour})


@login_required
def edit_review(request, review_id):
	review = get_object_or_404(Review, pk=review_id, user=request.user)

	if request.method == "POST":
		form = ReviewForm(request.POST)

		if form.is_valid():
			review.review = form.cleaned_data.get("review")
			review.rating = form.cleaned_data.get("rating")
			review.save()

			tour = review.tour
			tour.update_rating()

			messages.success(request, "The review was updated successfully!")

			return redirect(reverse("bookings"))
	else:
		form = ReviewForm(instance=review)

	return render(request, "reviews/edit_review.html", {"form": form})
