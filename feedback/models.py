from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from branch.models import Branch
from users.models import Customer

class Feedback(models.Model):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE)
    name = models.OneToOneField(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],default=1
    )
    feedback = models.CharField(max_length=255, blank=False, null=False)
    datetime_given = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_given"]