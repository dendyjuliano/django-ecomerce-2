from django.urls import path
from .views import IndexView,ShopView,ContactView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/',ShopView.as_view(),name='shop'),
    path('contact/',ContactView.as_view(),name='contact'),
]
