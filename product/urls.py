from django.urls import path

from .views import home_view, product_details_view

app_name = "product"
urlpatterns = [
    path("", home_view, name="home"),
    path("products/<slug:slug>", product_details_view, name="product_details"),
]
