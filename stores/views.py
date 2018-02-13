from django.shortcuts import render

from django.http import HttpResponse
from .models import Store
from .models import Product
# Create your views here.

def index(request):
    store_list = Store.objects[1:3]
    output = ','.join([q.store_name for q in store_list])
    return HttpResponse(output)


