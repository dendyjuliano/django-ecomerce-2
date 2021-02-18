from django.urls import path, include
from .views import (
    IndexView,
    ShopView,
    ContactView,
    ProductDetailView,
    cart,
    cart_add,
    cart_remove,
    cart_increment,
    cart_decrement,
)

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('detail_product/<slug>/',
         ProductDetailView.as_view(), name='detail_product'),
    path('cart/', cart, name='cart'),
    path('cart/cart-remove/<int:id>',
         cart_remove, name='cart-remove'),
    path('cart/cart-add/<int:id>', cart_add, name='cart-add'),
    path('cart/cart-increment/<int:id>',
         cart_increment, name='cart-increment'),
    path('cart/cart-decrement/<int:id>',
         cart_decrement, name='cart-decrement'),
]
