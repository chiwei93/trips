from django.shortcuts import render, get_object_or_404
from .models import Tour

# Create your views here.


def tours(request):
    tours = Tour.objects.all()
    tours_list = []

    for tour in tours:
        tours_list.append((tour, tour.images.all()[0]))

    return render(request, 'tours/tours.html', {
        "current_page": "tours",
        "tours": tours_list,
    })


def single_tour(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    images = tour.images.all()
    locations = tour.locations.all()
    reviews = tour.reviews.all()

    locations_names = []
    locations_coords = []

    for location in locations:
        locations_names.append(location.location_name)
        locations_coords.append(
            {"lat": location.latitude, "lng": location.longitudes, "name": location.location_name})

    return render(request, 'tours/tour.html', {
        "tour": tour,
        "images": images,
        "locations_names": locations_names,
        "locations_coords": locations_coords,
        "reviews": reviews,
        "numbers": [1, 2, 3, 4, 5]
    })
