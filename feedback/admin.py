from django.contrib import admin
from .models import Feedback
# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ("branch","name","rating","feedback")
    list_display = ("id","branch","name","rating","feedback","datetime_given")