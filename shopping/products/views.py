from django.shortcuts import render
from django.http import HttpResponse
from .models import product_db
# Create your views here.
import pandas as pd
import names


def product(request, *args, **kwargs):
    items = product_db.objects.all()
    print(request.method)
    return render(request, 'products/home.html', {'items': items})

def product_list(request, id,*args, **kwargs):
    items = product_db.objects.get(id=id)
    return HttpResponse(f'id: {items.id} , content: {items.content} , price: {items.price}')


