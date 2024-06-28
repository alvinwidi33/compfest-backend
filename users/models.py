from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class User(AbstractUser):
    ROLES = [
        ("Customer", "Customer"),
        ("Admin", "Admin")
    ]
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    username = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    role = models.CharField(max_length=255, choices=ROLES, default="Customer")
    phone_number = models.CharField(max_length=255, blank=False)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Customer(models.Model):
    STATUS = [
        ("Member", "Member"),
        ("Not Member", "Not Member")
    ] 
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_user')
    status = models.CharField(max_length=255, choices=STATUS, default="Not Member")

class Admin(models.Model):
    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_user')