from django.urls import path

from .views import cart_details_view

app_name = "cart"
urlpatterns = [path("<int:pk>/", cart_details_view, name="cart_details")]
