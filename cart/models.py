from django.db import models

from product.models import Product
from customer.models import Customer


class CartProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_cartproducts"
    )
    cart = models.ForeignKey(
        "Cart", on_delete=models.CASCADE, related_name="cart_cartproducts"
    )
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f"CartProduct - {self.product.name}.  Total_price = ${self.total_price}"


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_carts"
    )
    qty = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    in_order = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.customer.id}'s cart final_price = ${self.final_price}"
