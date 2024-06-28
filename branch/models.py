from django.db import models
from django.utils import timezone

class Branch(models.Model):
    branch_name = models.CharField(max_length=255, blank=False, null=False)
    branch_location = models.CharField(max_length=255, blank=False, null=False)
    image=models.CharField(max_length=2048, blank=False, null=False)
    opening_time = models.TimeField(default=timezone.localtime().replace(hour=9, minute=0), verbose_name='Opening Time', editable=True)
    closing_time = models.TimeField(default=timezone.localtime().replace(hour=21, minute=0), verbose_name='Closing Time', editable=True)

    class Meta:
        ordering =["branch_name"]