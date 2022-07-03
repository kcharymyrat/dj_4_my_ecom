from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    customer = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_customer"
    )
