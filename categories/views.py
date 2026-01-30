from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer


class CategoryListAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        queryset = Category.objects.filter(
            parent=None,
            is_active=True
        )

        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "success": True,
            "message": "Categories fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
