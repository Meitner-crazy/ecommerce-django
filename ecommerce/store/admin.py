from django.contrib import admin

# Register your models here.
from . models import Category, Product

# admin.site.register(Category)

# admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
#while I edit the name of the category, the slug will be automatically typed in as the name by default
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}