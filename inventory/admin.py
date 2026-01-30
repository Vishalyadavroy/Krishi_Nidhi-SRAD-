from django.contrib import admin
from .models import Warehouse, Inventory, StockMovement


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'state', 'is_active')
    search_fields = ('name', 'district')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('variant', 'warehouse', 'stock_quantity', 'reserved_quantity')
    list_filter = ('warehouse',)


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'movement_type', 'quantity', 'created_at')
    list_filter = ('movement_type',)

# Register your models here.
