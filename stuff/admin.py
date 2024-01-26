from django.contrib import admin
from .models import Books, Order, OrderItem, ShippingAddress
# Register your models here.

admin.site.register(Books)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

