from django.db.models.lookups import IContains
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Contact, Product, ComboProduct
from categorie.models import Category
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):  #view for index page homepage
    category = Category.objects.raw(
        'SELECT * FROM categorie_category ORDER BY random() limit 4'
    )  #show only 4 category on home page
    
    combo_product = ComboProduct.objects.raw(
            'SELECT * FROM product_comboproduct ORDER BY random() limit 4'
    )  #show only 4 combo product on home page

    if request.method == "POST":  #validation for contact form
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        inquiry = request.POST.get('inquiry')
        contact = Contact(firstname=name,
            contact_no=contact_no,
            email=email,
            message=inquiry)
        contact.save()
        messages.success(request, 'Thanks for contacting us your message has been send')
        return render(request, 'index.html')    
    context={       #pass all the key and value here
        'combo_product':combo_product,
        'category':category,
    }
    return render(request, 'index.html', context)  #rendering index.html page

def category(request):  #views for category page
    #getting all category by staticmethod from model
    category = Category.get_all_categories()  #fetching all category from database and oreder it by id
        
    context = {     #pass the key and value given below
        'category': category,
    }
    return render(request, 'category.html', context)        #rendering category.html

def product(request):  #view for product page
    products = None  #define product as none first
    categoryId = request.GET.get(
        'category'
    )  #assign category a id which is come from path by linking the page
    if categoryId:  # validation if category id is there
        products = Product.get_all_product_by_category(
            categoryId
        )  # it will show product by filtter which have same category id
    else:
        products = Product.get_all_products()  #otherwise it shows all product
    data = {  #pass the key and value given below
        'products': products,
    }
    return render(request, 'products.html', data)  #rendering product.html

def search(request):
    products=None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword'] 
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(product_name__icontains=keyword))      
    context={
        'products': products,
    }
    return render(request, 'products.html',context)  #rendering product.html