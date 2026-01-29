from django.contrib import admin
from .models import Product
from .models import Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = (
        "id",
        "company_name",
        "composition",
        "category",
        "brand",
        "price",
        "quantity",
        "unit",
        "is_active",
        "created_by",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
        "brand",
        "created_at",
    )

    search_fields = ("id",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")