from django.db import models
# from users.models import User
from categories.models import Category


# class Product(models.Model):

#     CATEGORY_CHOICES = (
#         ("SEED", "Seed"),
#         ("PESTICIDE", "Pesticide"),
#         ("INSECTICIDE", "Insecticide"),
#     )

#     # ✅ Replaced `name` with `company_name`
#     company_name = models.CharField(max_length=255)
    
#     # ✅ New field for composition
#     composition = models.TextField(blank=True)

#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     brand = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     unit = models.CharField(max_length=50)
#     quantity = models.PositiveIntegerField()

#     is_active = models.BooleanField(default=True)

#     created_by = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         related_name="products"
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.company_name
    
    

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)
#     is_active = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#this model is based on the bighaat


class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)

    categories = models.ManyToManyField(
        Category,
        related_name='products'
    )

    crops = models.ManyToManyField(
        Crop,
        related_name='products',
        blank=True
    )

    description = models.TextField()
    composition = models.TextField(blank=True)

    dosage = models.CharField(
        max_length=255,
        help_text="Dosage per acre or litre"
    )

    application_method = models.CharField(
        max_length=255,
        help_text="Soil / Foliar / Drip"
    )

    safety_period = models.CharField(
        max_length=100,
        blank=True,
        help_text="Waiting period after application"
    )

    is_restricted = models.BooleanField(
        default=False,
        help_text="Requires prescription or special approval"
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )

    pack_size = models.CharField(
        max_length=50,
        help_text="500ml, 1L, 5kg"
    )

    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    gst_percentage = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('product', 'pack_size')

    def __str__(self):
        return f"{self.product.name} - {self.pack_size}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', 'created_at']

    def save(self, *args, **kwargs):
        if self.is_primary:
            ProductImage.objects.filter(
                product=self.product,
                is_primary=True
            ).update(is_primary=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product.name}"
