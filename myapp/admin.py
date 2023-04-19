from django.contrib import admin
from.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['image','title','description','qty','price','date']
    search_fields=['title','description']

admin.site.register(Product,ProductAdmin)