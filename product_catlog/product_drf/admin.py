from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'is_active', 'brand', 'category', 'is_deleted')

admin.site.register(Product, ProductAdmin)