from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import OrderItem
# Create your views here.

# def calculate():
#     x =1 
#     y = 2
#     return x + y

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
    
    return render(request, 'hello.html', {'name': 'Rahman', 'products': list(queryset)})