from django.db import models

# Create your models here.
from django.db import  models
from products.models import ProductVariant



class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)


    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.district}"
    
class Inventory(models.Model):
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='inventory'
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='inventory'
    )

    stock_quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('variant', 'warehouse')

    def available_stock(self):
        return self.stock_quantity - self.reserved_quantity

    def __str__(self):
        return f"{self.variant} @ {self.warehouse}"


class StockMovement(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    RESERVE = 'RESERVE'
    RELEASE = 'RELEASE'

    MOVEMENT_TYPE_CHOICES = [
        (IN, 'Stock In'),
        (OUT, 'Stock Out'),
        (RESERVE, 'Reserve'),
        (RELEASE, 'Release'),
    ]

    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='movements'
    )

    movement_type = models.CharField(
        max_length=10,
        choices=MOVEMENT_TYPE_CHOICES
    )

    quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type} - {self.quantity}"
