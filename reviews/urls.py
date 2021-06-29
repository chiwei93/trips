from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.reviews, name="reviews"),
    path("new/<slug:slug>", views.add_review, name="new_review"),
    path("edit/<int:review_id>", views.edit_review, name="edit_review"),
]
