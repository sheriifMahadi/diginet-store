
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify
from stores.forms import ProductForm
from stores.models import Category, Product, Order, OrderItem

from .models import Users


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    context = {'user': user, "products": products}
    return render(request, 'users/vendor_detail.html', context)

@login_required
def vendor_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    orders = OrderItem.objects.filter(product__user=request.user)
    
    context = {"products": products, "orders": orders}
    return render(request, 'users/vendor_store.html', context)

@login_required
def store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'A new product has been added to store')
            return redirect('vendor_store')

    else:
        form = ProductForm()

    context = {"form":form, "title": "Add product"}
    return render(request, 'users/add_product.html', context)

def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Product has been updated')

    
            return redirect('vendor_store')
    else:
        form = ProductForm(instance=product)

    context = {"form":form, "title": "Edit product"}
    return render(request, 'users/add_product.html', context)

@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'Product has been deleted')
    return redirect('vendor_store')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            user = Users.objects.create(user=user)

            return redirect('homepage')
    else:
        form = UserCreationForm()
    context = {'form': form}

    return render(request, 'users/signup.html', context)

@login_required
def myaccount(request):
    return render(request, 'users/myaccount.html')
