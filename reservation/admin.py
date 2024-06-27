from django.contrib import admin
from .models import Reservation
# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    fields=("name","branch","type_of_service","datetime_start","datetime_end","is_done")
    list_display = ("id","name","branch","type_of_service","datetime_start","datetime_end","is_done")