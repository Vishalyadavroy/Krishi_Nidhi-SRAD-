from rest_framework import serializers
from .models import Product , ProductVariant , Crop  ,ProductImage
# from .models import Category

# class ProductSerializer(serializers.ModelSerializer):
#     created_by = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Product
#         fields = [
#             "id",
#             "company_name",
#             "composition",
#             "category",
#             "brand",
#             "description",
#             "price",
#             "unit",
#             "quantity",
#             "is_active",
#             "created_by",
#             "created_at",
#             "updated_at",
#         ]
#         read_only_fields = ("created_by", "created_at", "updated_at")

#     def validate_price(self, value):
#         if value <= 0:
#             raise serializers.ValidationError("Price must be greater than zero.")
#         return value

#     def validate_quantity(self, value):
#         if value <= 0:
#             raise serializers.ValidationError("Quantity must be greater than zero.")
#         return value
    
    
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["id", "name", "description"]





class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['id', 'name']



class ProductVariantSerializer(serializers.ModelSerializer):
    discount_percentage = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = [
            'id',
            'pack_size',
            'mrp',
            'selling_price',
            'gst_percentage',
            'discount_percentage'
        ]

    def get_discount_percentage(self, obj):
        if obj.mrp > obj.selling_price:
            return round(
                ((obj.mrp - obj.selling_price) / obj.mrp) * 100, 2
            )
        return 0

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image',
            'is_primary'
        ]



class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    crops = CropSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'brand',
            'description',
            'composition',
            'dosage',
            'application_method',
            'safety_period',
            'is_restricted',
            'primary_image',
            'images',
            'variants',
            'crops'
        ]

    def get_primary_image(self, obj):
        image = obj.images.filter(
            is_primary=True,
            is_active=True
        ).first()
        return image.image.url if image else None



