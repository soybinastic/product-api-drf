from django.contrib import admin
from .models import ProductCategory, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(ProductCategory)
