from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin): #make class for admin panel
    list_display=['id','category_name','image'] #display all the list from table

admin.site.register(Category,CategoryAdmin) #register the table and class