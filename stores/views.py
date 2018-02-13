from django.shortcuts import render

from django.http import HttpResponse
from .models import Store
from .models import Product
# Create your views here.

def index(request):
    store_list = Store.objects.all()
    output = ','.join([q.store_name for q in store_list])
    return HttpResponse(output)

def product_list(request, Store_id):
    products = Product.objects.filter(store_id=Store_id)
    output= ','.join([q.product_name for q in products])
    return HttpResponse(output)


