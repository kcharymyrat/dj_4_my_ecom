from django.shortcuts import redirect, render

from customer.models import Customer

from .models import Order
from .forms import OrderModelForm

from cart.models import Cart


def order_details_view(request, *args, **kwargs):
    cart = Cart.objects.get(pk=request.GET.get("cart_id"))
    user_customer_id = request.user.user_customer.id
    cart_customer_id = cart.customer.id
    print("cart =", cart)
    print("user_customer_id =", user_customer_id)
    print("cart_customer_id =", cart_customer_id)
    form = OrderModelForm(request.POST or None)
    if form.is_valid() and user_customer_id == cart_customer_id:
        # obj = form.save(commit=False)
        cleaned_form = form.cleaned_data
        cleaned_form["customer"] = Customer.objects.get(id=user_customer_id)
        cleaned_form["cart"] = cart
        Order.objects.create(
            cart=cart,
            customer=cleaned_form.get("customer"),
            address=cleaned_form.get("address"),
        )
        cart.in_order = True
        cart.save()
        print(cleaned_form)
        return redirect("/")
    return render(request, "order/order_details.html", {"form": form})
