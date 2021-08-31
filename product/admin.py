from django.contrib import admin
from .models import Contact, Product, ComboProduct  #import all table class from model


# Register your models here.
class ProductAdmin(admin.ModelAdmin):  #define class
    list_display = [
        'id', 'product_name','productqt1','qty1_price','productqt2','qty2_price', 'image', 'is_availabel',
        'category', 'category_id'
    ]  #listing the table


admin.site.register(Product, ProductAdmin)  #register to admin site


class ComboProductAdmin(admin.ModelAdmin):  #define class
    list_display = ['product_name', 'product_link', 'description',
                    'image']  #listing the table


admin.site.register(ComboProduct, ComboProductAdmin)  #register to admin site


class ContactAdmin(admin.ModelAdmin):  #define class
    list_display = ['id', 'firstname', 'contact_no', 'email',
                    'message']  #listing the table


admin.site.register(Contact, ContactAdmin)  #register to admin site
