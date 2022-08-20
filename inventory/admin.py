from django.contrib import admin
from .models import Product, Category, Brand, Stock
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at','updated_at','created_at_time','updated_at_date']

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Stock)