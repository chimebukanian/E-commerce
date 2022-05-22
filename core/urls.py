from django.urls import path
from .views import Home, Checkout, Product

app_name='core'

urlpatterns=[
    path('', Home, name='home'),
    path('checkout', Checkout, name='checkout'),
    path('product', Product, name='product')
]