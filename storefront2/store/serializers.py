from rest_framework import serializers
from decimal import Decimal
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)



#    name = serializers.CharField(max_length=100)
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # description = serializers.CharField(max_length=1000)
    # category = serializers.CharField(max_length=100)
    # tags = serializers.ListField(child=serializers.CharField(max_length=100))
    # likes = serializers.IntegerField()
    # is_on_sale = serializers.BooleanField()
    # views = serializers.IntegerField()