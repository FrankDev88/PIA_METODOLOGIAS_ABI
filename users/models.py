# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CLIENT = 'client'
    STAFF = 'staff'
    ROLE_CHOICES = [
        (CLIENT, 'Cliente'),
        (STAFF, 'Staff'),
    ]
    
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=CLIENT,
    )

    def __str__(self):
        return self.username
