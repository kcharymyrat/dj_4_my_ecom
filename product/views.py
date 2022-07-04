from decimal import Decimal
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
    print(request.GET.get("qty"))

    context = {}
    product = Product.objects.filter(slug=slug)

    if product.exists():
        context = {"product": product.first()}

    if request.GET.get("product"):
        product_for_cart = Product.objects.get(slug=request.GET.get("product"))
        customer = Customer.objects.get(customer=request.user)
        carts = customer.customer_carts.filter(in_order=False)
        print("carts =", carts, carts.exists())
        if carts.exists():
            cart = carts[0]
            print("cart =", cart)
        else:
            cart = Cart.objects.create(customer=customer)

        print(
            "cart.cart_cartproductsfilter(product=product_for_cart) =",
            cart.cart_cartproducts.filter(product=product_for_cart),
            cart.cart_cartproducts.filter(product=product_for_cart).exists(),
        )

        if not cart.cart_cartproducts.filter(product=product_for_cart).exists():
            cart_item = CartProduct.objects.create(
                product=product_for_cart,
                cart=cart,
                qty=int(request.GET.get("qty")),
                total_price=Decimal(
                    int(request.GET.get("qty")) * product_for_cart.price
                ),
            )
            cart.qty += 1
        else:
            cart_item = cart.cart_cartproducts.filter(product=product_for_cart)[0]
            cart_item.qty = int(request.GET.get("qty"))
            print(cart_item.qty, type(cart_item.qty))
            print(product_for_cart.price, type(product_for_cart.price))
            cart_item.total_price = Decimal(cart_item.qty * product_for_cart.price)
        cart_item.save()

        cart_products = cart.cart_cartproducts.all()
        print("cart_products =", cart_products)
        cart_final_price = 0
        for cart_product in cart_products:
            cart_final_price += cart_product.total_price
        cart.final_price = Decimal(cart_final_price)
        cart.save()

    return render(request, "product/product_details.html", context)
