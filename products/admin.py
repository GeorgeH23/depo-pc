from django.contrib import admin
from .models import Product, Category, Favorite

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stars',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_products']

    def display_products(self, obj):
        products = obj.products.all()
        return ", ".join([str(product) for product in products])

    display_products.short_description = "Products"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite, FavoriteAdmin)
