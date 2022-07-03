from multiprocessing import context
from django.shortcuts import render

from cart.models import Cart, CartProduct
from customer.models import Customer

from .models import Category, Product


def home_view(request, *args, **kwargs):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"products": products, "categories": categories}
    return render(request, "product/index.html", context)


def product_details_view(request, slug, *args, **kwargs):
    print(request.GET.get("product"))
    context = {}
    product = Product.objects.filter(slug=slug)
    if product.exists():
        context = {"product": product.first()}
    if request.GET.get("product"):
        product_for_cart = Product.objects.get(slug=request.GET.get("product"))
        customer = Customer.objects.get(customer=request.user)
        cart = Cart.objects.create(
            customer=customer, final_price=product_for_cart.price
        )
        cart_item = CartProduct.objects.create(
            customer=customer,
            cart=cart,
            price=product_for_cart.price,
            final_price=product_for_cart.price,
        )
        cart_item.products.add(product_for_cart)
        cart_item.save()

    return render(request, "product/product_details.html", context)
