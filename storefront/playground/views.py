from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Order
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import OrderItem
from store.models import Customer
from django.db.models import Sum, Avg, Max, Min, Count
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count
from django.db.models import ExpressionWrapper, F, DecimalField
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from store.models import Collection
from django.db import transaction
from django.db import connection
# Create your views here.

# def calculate():
#     x =1 
#     y = 2
#     return x + y
# @transaction.atomic() / for all the queries
def say_hello(request):
    # return HttpResponse("Hello World!")
    # x = calculate()
    # query_sets = Product.objects.all()
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # prodexists = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(unit_price__range=(20, 30))
    # for products in query_sets:
    #     print(products)
    # queryset = Product.objects.filter(collection__id__range=(1,2,3))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(description__isnull=True)
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20) # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    # queryset = Product.objects.order_by('unit_price','-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # queryset = Customer.objects.annotate(is_id=F('id'))
    # queryset = Customer.objects.annotate(
    #     full_name=Func(
    #         F('first_name'),
    #         Value(' '),
    #         F('last_name'),
    #         function='CONCAT'
    #     )
    # )
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # queryset = Customer.objects.annotate(
    #       orders_count=Count('order')
    #  )
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price=discounted_price)
    # queryset =  TaggedItem.objects.get_tags_for(Product, 1)
    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # Collection.objects.filter(pk=11).update(
    #     title= 'Video Games',
    # )
    # collection = Collection(pk=11)
    # collection.delete()

    # collection.objects.filter(id__gt=5).delete()
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM store_product')
        for row in cursor.fetchall():
            print(row)
    return render(request, 'hello.html', {'name': 'Rahman',})