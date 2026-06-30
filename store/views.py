from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
import random

@csrf_exempt
def signup(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data["username"]
        password = data["password"]

        if User.objects.filter(username=username).exists():

            return JsonResponse({
                "status": "exists"
            })

        User.objects.create(
            username=username,
            password=password
        )

        return JsonResponse({
            "status": "success"
        })


@csrf_exempt
def login(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data["username"]
        password = data["password"]

        try:

            user = User.objects.get(
                username=username,
                password=password
            )

            return JsonResponse({
                "status": "success",
                "userid": user.id
            })

        except:

            return JsonResponse({
                "status": "failed"
            })
        
@csrf_exempt
def reset_password(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data["username"]
        new_password = data["password"]

        try:
            user = User.objects.get(username=username)
            user.password = new_password
            user.save()

            return JsonResponse({
                "status": "success"
            })

        except User.DoesNotExist:

            return JsonResponse({
                "status": "failed"
            })
from .models import Product

def products(request):

    products = Product.objects.all()

    data = []

    for p in products:

        data.append({

            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": float(p.price),
            "image": p.image

        })

    return JsonResponse(data, safe=False)

from django.http import JsonResponse
from .models import Product

def product_list(request):

    products = Product.objects.all()

    data = []

    for p in products:

        data.append({

            "id":p.id,

            "name":p.name,

            "price":float(p.price),

            "category":p.category,

            "image":p.image

        })

    return JsonResponse(data,safe=False)
from .models import Cart, Product, User
from django.http import JsonResponse

def add_cart(request, id):

    try:
        user = User.objects.first()   # Temporary user

        product = Product.objects.get(id=id)

        cart = Cart.objects.filter(user=user, product=product).first()

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=user,
                product=product,
                quantity=1
            )

        return JsonResponse({
            "message": "Product Added Successfully"
        })

    except Exception as e:

        return JsonResponse({
            "message": str(e)
        })
def cart_data(request):

    user = User.objects.first()

    cart = Cart.objects.filter(user=user)

    data = []

    for item in cart:

        data.append({

            "id": item.id,
            "name": item.product.name,
            "price": float(item.product.price),
            "image": item.product.image,
            "quantity": item.quantity

        })

    return JsonResponse(data, safe=False)
from django.shortcuts import get_object_or_404

def remove_cart(request,id):

    cart=get_object_or_404(Cart,id=id)

    cart.delete()

    return JsonResponse({

        "message":"Product Removed"

    })
from .models import Order

@csrf_exempt
def checkout(request):

    if request.method == "POST":

        data = json.loads(request.body)

        name = data.get("name")
        phone = data.get("phone")
        address = data.get("address")

        user = User.objects.first()

        cart = Cart.objects.filter(user=user)

        if not cart.exists():

            return JsonResponse({
                "status":"failed",
                "message":"Cart is Empty"
            })

        total = 0

        for item in cart:
            total += float(item.product.price) * item.quantity

        tracking = "PHA" + str(random.randint(10000,99999))

        Order.objects.create(
            user=user,
            total=total,
            payment_method="Pending",
            tracking_id=tracking,
            status="Order Placed"
        )

        request.session["name"] = name
        request.session["phone"] = phone
        request.session["address"] = address

        return JsonResponse({
            "status":"success"
        })
def payment_data(request):

    user = User.objects.first()

    cart = Cart.objects.filter(user=user)

    total = 0

    for item in cart:
        total += float(item.product.price) * item.quantity

    return JsonResponse({

        "name": request.session.get("name"),
        "phone": request.session.get("phone"),
        "address": request.session.get("address"),
        "total": total

    })
@csrf_exempt
def complete_payment(request):

    if request.method == "POST":

        data = json.loads(request.body)

        payment_method = data["payment_method"]

        user = User.objects.first()

        order = Order.objects.filter(user=user).last()

        if order:

            order.payment_method = payment_method
            order.status = "Payment Successful"
            order.save()

        Cart.objects.filter(user=user).delete()

        return JsonResponse({

    "status": "success",
    "message": "Payment Successful",
    "tracking_id": order.tracking_id

})
def tracking_data(request):

    user = User.objects.first()

    order = Order.objects.filter(user=user).last()

    if order:

        return JsonResponse({

            "tracking_id": order.tracking_id,
            "status": order.status

        })

    return JsonResponse({

        "tracking_id": "",
        "status": "No Order"

    })