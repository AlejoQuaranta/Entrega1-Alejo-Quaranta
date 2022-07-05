from django.contrib import admin
from products.models import Products, Categoria

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'SKU', 'active']

admin.site.register(Categoria)