from django.contrib import admin
from .models import Customer, Product, Order, ShippingAddress, OrderApproval

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderApproval)
admin.site.register(ShippingAddress)