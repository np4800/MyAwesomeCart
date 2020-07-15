from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.
def index(request):
    # product = Product.objects.all()
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # n=len(product)
    # print(product)
    # params = {'no_of_slides':nSlides,'range':range(nSlides),'product':product} ## Old params
    # allProds = [[product,range(1,nSlides),nSlides],[product,range(1,nSlides),nSlides]]
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = { item['category'] for item in catprods }
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod,range(1,nSlides),nSlides])

    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about (request):
    # params={'product_name':'Fossil','product_price':'9000','Category':'Accessories','Subcategory':'Watches'}
    product='Fossil'
    params={'purpose': 'Product Name', 'analyzed_text': product}
    return render(request,'shop/about.html',params)

def contact (request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,'shop/contact.html')

def tracker (request):
    product='Fossil'
    params={'purpose': 'Product Name', 'analyzed_text': product}
    return render(request,'shop/tracker.html',params)

def search (request):
    product='Fossil'
    params={'purpose': 'Product Name', 'analyzed_text': product}
    return render(request,'shop/search.html',params)

def productView (request,myid):
    product = Product.objects.filter(id=myid)
    params={'purpose': 'Product Name', 'product': product[0]}
    return render(request,'shop/productView.html',params)

def checkout (request):
    product='Fossil'
    params={'purpose': 'Product Name', 'analyzed_text': product}
    return render(request,'shop/checkout.html',params)
