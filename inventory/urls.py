from django.urls import path
from .views import VariantInventoryAPIView

urlpatterns = [
    path(
        'variant/<int:variant_id>/',
        VariantInventoryAPIView.as_view(),
        name='variant-inventory'
    ),
]
