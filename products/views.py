# from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework import generics
# from users.permissions import IsSeller ,IsOwnerOrReadOnly
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter
# from .pagination import ProductPagination
# from rest_framework.generics import ListAPIView
# from .models import Category
# from .serializers import CategorySerializer


# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.filter(is_active=True)
#     serializer_class = ProductSerializer
#     pagination_class = ProductPagination

#     filter_backends = [
#         DjangoFilterBackend,
#         SearchFilter,
#         OrderingFilter,
#     ]


#     filterset_fields = ["category", "brand"]
#     search_fields = ["company_name", "brand", "composition"]
#     ordering_fields = ["price", "created_at"]

#     permission_classes = [IsAuthenticated]

#     def get_permissions(self):
#         """Allow anyone to list, but only sellers can create"""
#         if self.request.method == 'POST':
#             return [IsSeller()]
#         return [AllowAny()]

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)



# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
#     queryset = Product.objects.all()


# class CategoryListView(ListAPIView):
#     queryset = Category.objects.filter(is_active=True)
#     serializer_class = CategorySerializer
#     permission_classes = [AllowAny]






#this is the bighaat backend approach 
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request):
        queryset = Product.objects.filter(
            is_active=True
        ).prefetch_related(
            'variants', 'crops', 'categories'
        )

        serializer = self.serializer_class(queryset, many=True)

        return Response({
            "success": True,
            "message": "Products fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class ProductDetailAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, pk):
        try:
            product = Product.objects.prefetch_related(
                'variants', 'crops'
            ).get(pk=pk, is_active=True)
        except Product.DoesNotExist:
            return Response({
                "success": False,
                "message": "Product not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(product)
        return Response({
            "success": True,
            "message": "Product details fetched",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
