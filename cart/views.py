from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Cart, CartProduct


def cart_details_view(request, pk, *args, **kwargs):
    cart = Cart.objects.get(pk=pk)
    print(cart)
    context = {"cart": cart}
    return render(request, "cart/cart_details.html", context)
