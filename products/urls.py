from django.urls import path
from .views import ProductListCreateView, ProductDetailView
from .views import CategoryListView

urlpatterns = [
    path("list/", ProductListCreateView.as_view(), name="product-list-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
]
