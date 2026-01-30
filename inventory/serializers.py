from rest_framework import serializers
from .models import Warehouse, Inventory


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    available_stock = serializers.IntegerField(
        source='available_stock',
        read_only=True
    )

    class Meta:
        model = Inventory
        fields = [
            'id',
            'warehouse',
            'stock_quantity',
            'reserved_quantity',
            'available_stock'
        ]
