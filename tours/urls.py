from django.urls import path

from . import views

urlpatterns = [
    path("", views.tours, name="tours"),
    path("<slug:slug>", views.single_tour, name="tour"),
]
