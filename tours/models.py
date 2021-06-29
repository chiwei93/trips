from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitudes = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return f"{self.location_name}"


class Image(models.Model):
    image_path = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.image_path}"


class Tour(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, db_index=True)
    duration = models.IntegerField()
    max_group_size = models.IntegerField()
    ratings = models.FloatField(default=0)
    ratings_number = models.IntegerField(default=0)
    price = models.FloatField()
    summary = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    locations = models.ManyToManyField(Location)
    images = models.ManyToManyField(Image)
    num_of_spots_left = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    def update_rating(self):
        reviews = self.reviews.all()
        avg_rating = reviews.aggregate(models.Avg("rating"))
        self.ratings = avg_rating.get("rating__avg")
        self.ratings_number = reviews.count()
        self.save()
