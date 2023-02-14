from django.urls import path, include
from .views import product,product_list

urlpatterns = [
    path('adddata/', product),
    path('product/<int:id>/',product_list),
    
]
