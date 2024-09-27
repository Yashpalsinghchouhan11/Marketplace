from django.contrib import admin
from .models import CustomUser,Product,Cart,Wishlist

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)