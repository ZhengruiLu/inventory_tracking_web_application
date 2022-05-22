from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product
# Create your views here.

def index(request):
    # items = Product.objects.all()
    # items = Product.objects.raw('SELECT * FROM dashboard_product')

    # context = {
    #     'items': items,
    # }

    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    return render(request, 'dashboard/product.html')

def order(request):
    return render(request, 'dashboard/order.html')