from django.contrib import admin
from .models.user import User
from .models.order import Order
from .models.order_product import OrderProduct
from .models.product import Product
from .models.provider import Provider

# Register your models here.

admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Product)
admin.site.register(Provider)
