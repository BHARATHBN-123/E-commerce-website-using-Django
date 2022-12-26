from django.shortcuts import render
from .models import product_db
# Create your views here.
import pandas as pd
import names


def product(request, *args, **kwargs):
    items = product_db.objects.all()
    print(request.method)
    return render(request, 'products/home.html', {'items': items})
