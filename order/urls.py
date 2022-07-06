from django.urls import path

from .views import order_details_view

app_name = "order"
urlpatterns = [
    path("", order_details_view, name="order_details"),
]
