from django.urls import path
from . import views

urlpatterns = [
    path("", views.bookings, name="bookings"),
    path("<int:booking_id>", views.single_booking, name="booking"),
    path("new/<slug:slug>", views.make_booking, name="new_booking"),
    path("confirm/<slug:slug>", views.confirm_booking, name="confirm_booking"),
    path("success/<slug:slug>", views.checkout_success, name="booking_success"),
    path("delete/<int:booking_id>", views.delete_booking, name="delete_booking"),
]
