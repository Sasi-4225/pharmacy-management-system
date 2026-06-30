from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def cart(request):
    return render(request, "add to cart.html")

def orders(request):
    return render(request, "orders.html")

def payment(request):
    return render(request, "payment.html")
def tracking(request):
    return render(request, "tracking.html")

def vitamins(request):
    return render(request, "Vitamins.html")

def diabetes(request):
    return render(request, "Diabetes.html")

def fever(request):
    return render(request, "Fever&infection.html")

def hair(request):
    return render(request, "Hair&SkinCare.html")

def thyroid(request):
    return render(request, "Thyroid.html")

def women(request):
    return render(request, "WomenCare.html")

def heart(request):
    return render(request, "Heart.html")

def bone(request):
    return render(request, "BoneHealth.html")

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", index),

    path("login/", login),

    path("home/", home),

    path("products/", products),

    path("cart/", cart),

    path("orders/", orders),

    path("payment/", payment),

    path("tracking/", tracking),

    path("vitamins/", vitamins),

    path("diabetes/", diabetes),

    path("fever-infection/", fever),

    path("hair-skin-care/", hair),

    path("thyroid/", thyroid),

    path("women-care/", women),

    path("heart/", heart),

    path("bone-health/", bone),

    path("", include("store.urls")),

]