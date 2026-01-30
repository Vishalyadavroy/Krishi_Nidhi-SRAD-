from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView
# from .views import CategoryListView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="product-list-create"),
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    # path("categories/", CategoryListView.as_view(), name="category-list"),
]
