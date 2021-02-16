from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from .models import Product, Category
from .filters import OrderProduct, SearchProduct

# Create your views here.


class IndexView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        product = Product.objects.all()
        data_search = SearchProduct(self.request.GET, queryset=product)
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
        context.update({
            'category_list': Category.objects.all()
        })
        return context
