from django.contrib import admin
from .models import *


# from .models import Product
# Need more columns to display then


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','product_image')

admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Product,ProductAdmin)


# admin.site.register(Catagory)
# admin.site.register(Product)

