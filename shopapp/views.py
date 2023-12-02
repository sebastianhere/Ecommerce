from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.core.paginator import Paginator


# Create your views here.


def Home(request):
    data = Products.objects.all()
    ct = Category.objects.all()
    pagination = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    total_page = page_obj.paginator.num_pages
    total_page_list = [n + 1 for n in range(total_page)]

    return render(request, 'index.html', { 'cato': ct, 'prods': page_obj, 'tot': total_page, 'num': total_page_list})


def About(request):
    return render(request,'about.html')


def News(request):
    return render(request,'news.html')


def Contact(request):
    return render(request,'contact.html')


def Categor(request):
    ct = Category.objects.all()
    return render(request, 'cat.html', {'obj': ct})



def Shop(request):

    return render(request,'shop.html')



def Productview(request, cname):
    prod = Products.objects.filter(catagory__name=cname)
    pagination = Paginator(prod,3)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    total_page = page_obj.paginator.num_pages
    total_page_list = [n + 1 for n in range(total_page)]
    return render(request, 'products.html', {'pros': prod, 'prods': page_obj, 'tot': total_page, 'num': total_page_list})



def Singleproduct(request,pname):
    prod = Products.objects.filter(pname=pname).first()
    print(prod)
    return render(request,'single-product.html',{'sin':prod})


def Searching(request):
    pro = None
    quary = None
    if 'q' in request.GET:
        quary = request.GET.get('q')
        pro = Products.objects.all().filter(Q(pname__icontains=quary)|Q(pro_desc__icontains=quary))
        print(pro,'a')
    return render (request,'search.html',{'qr':quary,'pr':pro})



def CartDetails(request,tot=0,count=0,ftot=0):
    cart_items = None
    try:
        ct = Cart.objects.get(cart_id=cart_id(request))
        cart_items = Items.objects.filter(cart=ct,active=True)
        print('cartitems',cart_items)

        for i in cart_items:
            tot+=(i.products.sell_price*i.quantity)
            count +=i.quantity
            ftot = tot + 45
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart_items,'tot':tot,'count':count,'ftot':ftot})

def cart_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id


class Product:
    pass


def add_cart(request,product_id):
    product=Products.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cart_id(request))
        cart.save()
    try:
        c_items=Items.objects.get(products=product,cart=cart)
        if c_items.quantity < c_items.products.stocks:
            c_items.quantity+=1
            c_items.save()
    except Items.DoesNotExist:
        c_items=Items.objects.create(products=product,quantity=1,cart=cart)
        c_items.save()
    return redirect('cartpage')

def min_cart(request,product_id):
    ct=Cart.objects.get(cart_id=cart_id(request))
    print('cart', ct)
    prod= get_object_or_404(Products,id=product_id)
    c_items=Items.objects.get(products=prod,cart=ct)
    if c_items.quantity > 1:
        c_items.quantity-= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect("cartpage")


def delete_cart(request,product_id):
    ct = Cart.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = Items.objects.get(products=prod, cart=ct)
    c_items.delete()
    return redirect("cartpage")


def Checkout(request):
    cart_items = None
    tot = 0
    cart_items = Items.objects.all()
    for i in cart_items:
        tot += (i.products.sell_price * i.quantity)
        ftot = tot + 45

    return render(request,'checkout.html',{'item':cart_items,'totalprice':tot,'ftot':ftot})









