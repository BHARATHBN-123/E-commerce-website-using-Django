from django.urls import path, include
from .views import product

urlpatterns = [
    path('adddata/', product),
]
