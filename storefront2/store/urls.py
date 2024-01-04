from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.PrtoductList.as_view()),
    path('products/<int:id>', views.PrtoductDetail.as_view()),
    path('collections/<int:pk>', views.collection_detail, name='collection-detail'),
    path('collections/', views.collection_list, name='collection-list'),
]
