from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.PrtoductDetail.as_view()),
    path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection-detail'),
    path('collections/', views.CollectionList.as_view()),
]
