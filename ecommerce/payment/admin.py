from django.contrib import admin
from . models import ShippingAddress


# Add class shipping address in the admin page
admin.site.register(ShippingAddress)