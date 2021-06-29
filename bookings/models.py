from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour

# Create your models here.


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    created_at = models.DateTimeField(auto_now_add=True)
    num_of_people = models.IntegerField()
    price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.tour.name} {self.user.username}"
