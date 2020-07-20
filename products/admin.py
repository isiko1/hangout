from django.contrib import admin
from .models import Product, Department

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'price',
        'department',
        'rating',
        'image_url',
        'image',
    )

    ordering = ('image',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Department, DepartmentAdmin)
