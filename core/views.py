from django.shortcuts import render
from .models import Item
# Create your views here.
def Home(request):
    context={
        'items':Item.objects.all()
    }
    return render(request, "home-page.html", context)

def Checkout(request):
    return render(request, "checkout-page.html")


def Product(request):
    return render(request, "product-page.html")