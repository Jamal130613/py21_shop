from django.contrib import admin
from applications.cart.models import Order, CartItem, Cart

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)

