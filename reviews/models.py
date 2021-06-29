from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour

# Create your models here.


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.tour} {self.rating}"
