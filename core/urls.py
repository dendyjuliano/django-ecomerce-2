from django.urls import path
from .views import IndexView,ShopView,ContactView,ProductDetailView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(r'^shop/$',ShopView.as_view(),name='shop'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('detail_product/<slug>/',ProductDetailView.as_view(),name='detail_product'),

]
