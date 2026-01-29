from django.db import models
from users.models import User


class Product(models.Model):

    CATEGORY_CHOICES = (
        ("SEED", "Seed"),
        ("PESTICIDE", "Pesticide"),
        ("INSECTICIDE", "Insecticide"),
    )

    # ✅ Replaced `name` with `company_name`
    company_name = models.CharField(max_length=255)
    
    # ✅ New field for composition
    composition = models.TextField(blank=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="products"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
