from django.contrib import admin

from .models import Product, ShoppingCart, ShoppingCartItem

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
