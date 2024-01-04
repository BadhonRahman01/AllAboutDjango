from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()  
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory','unit_price','price_with_tax','collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail',
    #     lookup_field='pk'
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product
    #     # return Product.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.inventory = validated_data.get('inventory', instance.inventory)
    #     instance.unit_price = validated_data.get('unit_price', instance.unit_price)
    #     instance.collection = validated_data.get('collection', instance.collection)
    #     instance.save()
    #     return instance
    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError('Title and description must be different from one another!')
    #     return data

#    name = serializers.CharField(max_length=100)
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # description = serializers.CharField(max_length=1000)
    # category = serializers.CharField(max_length=100)
    # tags = serializers.ListField(child=serializers.CharField(max_length=100))
    # likes = serializers.IntegerField()
    # is_on_sale = serializers.BooleanField()
    # views = serializers.IntegerField()