from django.db import models
from branch.models import Branch
from users.models import Customer

# Create your models here.
class Reservation(models.Model):
    SERVICE = [ 
        ("Haircuts and styling", "Haircuts and styling"),
        ("Manicure and pedicure", "Manicure and pedicure"),
        ("Facial treatments","Facial treatments")
        ]
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    type_of_service =models.CharField(max_length=255, choices=SERVICE, default="Haircuts and styling")
    datetime_reserve = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    class meta:
        ordering=["-datetime_reserve"]