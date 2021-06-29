from django.contrib import admin
from .models import Location, Image, Tour

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tour, TourAdmin)
admin.site.register(Location)
admin.site.register(Image)
