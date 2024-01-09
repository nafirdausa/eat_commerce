from django.contrib import admin

# Register your models here.
from .models import Category, Product, Contact_us, Order, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Brand)



@admin.register(Contact_us)
class Contact_bebas(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

# @admin.register(Order)
# class order_user(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity','price','address','phone','pincode','date')

