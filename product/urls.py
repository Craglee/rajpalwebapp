from django.urls import path
from . import views #import views
urlpatterns = [
    path('',views.home,name='home'),    #blank path for homepage which come from project urls
    path('category',views.category, name="categorypage"),   #category path to get category page
    path('product',views.product, name="productpage"),      #product path to get product page
    path('search',views.search,name='search'),
]
