from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True) #database model for category name
    image = models.ImageField(upload_to="photos/category", blank=True) #database model for category image

    @staticmethod  # this staticmethod return all category 
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):  #returning self str category name
        return self.category_name

    @property
    def get_photo_url(self):   # if category dont have image bydefault it shows else image otherwise if will run
        if self.image and hasattr(self.image, 'url'):   #this code is returning image url
            return self.image.url
        else:
            return "/static/images/Img-demo.jpg"