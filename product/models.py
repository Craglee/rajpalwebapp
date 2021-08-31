from django.db.models.fields import IntegerField
from categorie.models import Category
from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):  #model table for products
    product_name = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255, blank=True,unique=False)
    qty1_price = models.IntegerField(blank=True)
    qty2_price = models.IntegerField(blank=True)
    productqt1 = models.CharField(max_length=50, default="50 GM",blank=True)
    productqt2 = models.CharField(max_length=50, default="250 GM",blank=True)
    image = models.ImageField(upload_to='photos/products', blank=True)
    is_availabel = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)  #getting category by use of foreignkey
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    @property
    def get_photo_url(self):   # if category dont have image bydefault it shows else image otherwise if will run
        if self.image and hasattr(self.image, 'url'):   #this code is returning image url
            return self.image.url
        else:
            return "/static/images/Img-demo.jpg"

    @staticmethod  # staticmethod to get all product
    def get_all_products():
        return Product.objects.all()

    @staticmethod  # staticmethod to get all product by category id for productpage
    def get_all_product_by_category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):  #returning self str product name
        return self.product_name

class ComboProduct(models.Model):  #combo product model table
    product_name = models.CharField(max_length=255, unique=True)
    product_link = models.CharField(max_length=255, unique=True,blank=True)
    description = models.TextField(max_length=500, blank=True)
    quantity = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos/products',blank=True)

class Contact(models.Model):  #contact model table
    firstname = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=10000)
