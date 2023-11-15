from itertools import product
from django.shortcuts import render
from stores.models import Product
# Create your views here.
def home(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]
    context = {"products": products}
    return render(request, "main/home.html", context)

def about(request):
    return render(request, "main/about.html")