from django.contrib import admin
from .models import Product , ProductImage

# Register your models here.
from django.contrib import admin
from .models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'category',
        'brand',
        'is_active',
        'created_at'
    )

    list_filter = (
        'category',
        'brand',
        'is_active'
    )

    search_fields = (
        'name',
        'description'
    )

    ordering = ('-created_at',)

 
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product',
        'is_primary',
        'created_at'
    )

    list_filter = (
        'is_primary',
    )

    search_fields = (
        'product__name',
    )

    ordering = ('-created_at',)
