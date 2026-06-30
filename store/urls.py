from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login-api/", views.login, name="login_api"),
    path("reset-password/", views.reset_password, name="reset_password"),
    path("products/", views.products, name="products"),
    path("api/products/",views.product_list),
    path("add-cart/<int:id>/", views.add_cart),
    path("cart-data/", views.cart_data),
    path("remove-cart/<int:id>/",views.remove_cart),
    path("checkout/", views.checkout),
    path("payment-data/", views.payment_data),
    path("complete-payment/", views.complete_payment),
    path("tracking-data/", views.tracking_data),
]