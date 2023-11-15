from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .cart import Cart
from .forms import OrderForm
from .models import Category, Product, Order, OrderItem
from django.contrib import messages

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('homepage')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')

def cart_view(request):
    cart = Cart(request)
    context = {"cart": cart}
    return render(request, 'stores/cart_view.html', context)

@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        print('x')
        form = OrderForm(request.POST)
        
        if form.is_valid():
            total_price = 0
            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])
            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()
            
            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
            cart.clear()
            return redirect('myaccount')
    else:
        form = OrderForm()

    form = OrderForm()
    context = {"cart": cart, "form": form}
    return render(request, 'stores/checkout.html', context)

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(title__icontains=query).filter(status=Product.ACTIVE)
    context = {"query": query, "products": products}
    return render(request, 'stores/search.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    context = {"category": category, "products": products}

    return render(request, 'stores/category_detail.html', context)


def product_detail(request, category_slug, slug):
    cart = Cart(request)
    print(cart.get_total_cost())
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE )
    context = {"product": product}
    return render(request, 'stores/product_detail.html', context)

