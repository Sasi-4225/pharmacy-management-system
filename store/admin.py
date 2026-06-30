from django.contrib import admin
from .models import User, Product, Cart, Order

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "tracking_id",
        "user",
        "total",
        "payment_method",
        "status",
        "created_at"
    )

    list_filter = ("status",)

    search_fields = (
        "tracking_id",
        "user__username"
    )