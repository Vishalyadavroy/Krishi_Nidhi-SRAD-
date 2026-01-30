from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Inventory
from .serializers import InventorySerializer


class VariantInventoryAPIView(GenericAPIView):
    serializer_class = InventorySerializer

    def get(self, request, variant_id):
        inventory_qs = Inventory.objects.filter(
            variant_id=variant_id,
            warehouse__is_active=True
        )

        serializer = self.serializer_class(inventory_qs, many=True)

        return Response({
            "success": True,
            "message": "Inventory fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
