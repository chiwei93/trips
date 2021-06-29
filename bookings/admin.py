from django.contrib import admin
from .models import Booking


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Booking, BookAdmin)
