from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products"
    )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f"{self.name} from Category: {self.category.name}"

    def get_absolute_url(self):
        return reverse("product:product_details", kwargs={"slug": self.slug})
