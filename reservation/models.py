from django.db import models
from branch.models import Branch
from users.models import Customer
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
class Reservation(models.Model):
    SERVICE_CHOICES = [
        ("Haircuts and styling", "Haircuts and styling"),
        ("Manicure and pedicure", "Manicure and pedicure"),
        ("Facial treatments", "Facial treatments"),
    ]

    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    type_of_service = models.CharField(max_length=255, choices=SERVICE_CHOICES, default="Haircuts and styling")
    datetime_start = models.DateTimeField(default=timezone.now)
    datetime_end = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],default=0
    )
    feedback = models.CharField(max_length=1024, blank=True,null=True)
    class Meta:
        ordering = ["-datetime_start"]

    def __str__(self):
        return f"Reservation for {self.name} at {self.branch} ({self.datetime_start} to {self.datetime_end})"
