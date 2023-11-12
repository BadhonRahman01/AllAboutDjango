from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
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
    queryset = Product.objects.filter(description__isnull=True)
    return render(request, 'hello.html', {'name': 'Rahman', 'products': list(queryset)})