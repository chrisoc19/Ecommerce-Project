from django.contrib import admin
from .models import Product, Category, Product_sale


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
# Register your models here.
admin.site.register(Product)
admin.site.register(Product_sale)
