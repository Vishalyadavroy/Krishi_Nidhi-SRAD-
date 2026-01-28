from django.db import models

from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from .manager import UserManager

import uuid
from django.db import models
from django.utils import timezone




LANGUAGE_CHOICES = (
    ("English", "English"),
    ("Hindi", "Hindi"),
)


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('FARMER', 'Farmer'),
        ('WHOLESALER', 'Wholesaler'),
        ('RETAILER', 'Retailer'),
        ('COMPANY', 'Company'),
        ('ADMIN', 'Admin'),
    )

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        db_index=True
    )
    phone = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        db_index=True
    )

    name = models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='FARMER'
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='English'
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.email or self.phone or f"User #{self.id}"


# users/models.py
class OTP(models.Model):
    phone = models.CharField(max_length=15)
    code = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=5)
