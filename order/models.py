from django.db import models

from cart.models import Cart
from customer.models import Customer


class Order(models.Model):
    CREATED = "created"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    ON_STALE = "on stale"
    REFUNDED = "refunded"

    STATUS_CHOICES = (
        (CREATED, "Created"),
        (PAID, "Paid"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
        (ON_STALE, "On stale"),
        (REFUNDED, "Refunded"),
    )

    cart = models.OneToOneField(
        Cart, related_name="cart_order", on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_orders"
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=CREATED,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"Order #{self.id}. Customer: {self.customer}. Cart: {self.cart}"
