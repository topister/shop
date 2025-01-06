from django.contrib import admin
from .models import Products
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

admin.site.register(Products, ProductAdmin)