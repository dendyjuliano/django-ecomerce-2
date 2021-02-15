from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from .models import Product

# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = "home/index.html"


class ShopView(ListView):
    model = Product
    template_name = "home/shop.html"

class ContactView(View):
    def get(self,*args,**kwargs):
        return render(self.request,"home/contact.html")
