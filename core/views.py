from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from .models import Product, Category
from .filters import OrderProduct, SearchProduct
from django.contrib.auth.decorators import login_required
from .cart import Cart
from decimal import Decimal

# Create your views here.


class IndexView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        product = Product.objects.all()
        data_search = SearchProduct(self.request.GET, queryset=product)
        cart = Cart(self.request)
        context.update({
            'category_list': Category.objects.all(),
            'data_search': data_search,
        })
        return context


class ShopView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = "home/shop.html"

    def get_context_data(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        product = Product.objects.all()
        data_filter = OrderProduct(self.request.GET, queryset=product)
        data_search = SearchProduct(self.request.GET, queryset=product)
        cart = Cart(self.request)
        context.update({
            'category_list': Category.objects.all(),
            'data_filter': data_filter,
            'data_search': data_search,
        })
        return context


class ContactView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "home/contact.html")


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "home/detail_product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = Product.objects.all()
        data_filter = OrderProduct(self.request.GET, queryset=product)
        data_search = SearchProduct(self.request.GET, queryset=product)
        cart = Cart(self.request)
        context.update({
            'category_list': Category.objects.all(),
            'data_filter': data_filter,
            'data_search': data_search,
        })
        return context

# add cart


@login_required
def cart(request):
    cart = Cart(request)
    product = Product.objects.all()
    data_search = SearchProduct(request.GET, queryset=product)

    context = {
        'cart': cart,
        'data_search': data_search
    }
    return render(request, 'home/cart.html', context)


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)

    cart.add(product, Decimal(product.get_price))
    return redirect('core:cart')


@login_required
def cart_remove(request, id):
    product = Product.objects.get(id=id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('core:cart')


@login_required
def cart_increment(request, id):
    product = Product.objects.get(id=id)
    quantity = 1
    cart = Cart(request)
    cart.increment(product, quantity)
    return redirect('core:cart')


@login_required
def cart_decrement(request, id):
    product = Product.objects.get(id=id)
    quantity = 1
    cart = Cart(request)
    cart.decrement(product, quantity)
    return redirect('core:cart')
