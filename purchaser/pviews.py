from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import feedback, feedbackForm, paymentForm
from .forms import Userform
# from .models import SignUpForm
from shopOwner.models import requests
from django.shortcuts import render,redirect
from .models import SignUpForm
from cartpage.models import cartproductForm,cartproducts
from shopOwner.models import requests
from employee.models import products
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,user_logged_out
)
from django.contrib.auth.decorators import login_required

#view all prdoucts to purchaser
def purchaserhome(request):
    #return render(request,"purchaser/purchaserhomepage.html")
        allproducts = products.objects.all()
        return render(request, "purchaser/purchaserhomepage.html", {"products": allproducts})


#view all prdoucts to purchaser
def home(request):
    #return render(request,"purchaser/purchaserhomepage.html")
        allproducts = products.objects.all()
        return render(request, "home.html")


#view details of a specific product to purchaser
def details(request,product_id):
    allproduct = products.objects.get(id=product_id)
    filtercomments = feedback.objects.filter(product=allproduct)
    return render(request, "purchaser/productDetails.html", {"product": allproduct,"comments":filtercomments})
    #return render(request,"purchaser/productDetails.html")


def add(request,user_id,product_id):
    cartOwner = User.objects.get(id=user_id)
    myProduct = products.objects.get(id=product_id)
    myProduct.numberOfItems = myProduct.numberOfItems - 1
    myProduct.save()
    newcart = cartproducts(name=myProduct.name, price=myProduct.price,barcode=myProduct.barcode,cartOwner=cartOwner)
    newcart.save()
    return redirect("http://127.0.0.1:8000/purchaser/details/" + product_id)

#signUp
def signUp (request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
             user=form.save()
             auth_login(request, user)
             group = Group.objects.get(name='purchasers')
             user.groups.add(group)
             return redirect('purchaserhomepage')
    else:
        form=SignUpForm()
    return render(request,'purchaser/signup1.html',{'form':form})



def search(request):
    searchForm = request.POST
    searchText = searchForm["myText_Box"]
    product = products.objects.filter(name__contains=searchText)

    return render(request, "purchaser/purchaserhomepage.html", {"products": product})



def searchprice(request):
    searchForm = request.POST
    searchText = searchForm["price"]
    searchnumber=int(searchText)


    if searchnumber==100:
        product = products.objects.filter(price__range=(100,1000))
        return render(request, "purchaser/purchaserhomepage.html", {"products": product})

    elif searchnumber==10:
        product = products.objects.filter(price__range=(10, 100))
        return render(request, "purchaser/purchaserhomepage.html", {"products": product})

    elif searchnumber==1000 :
        product = products.objects.filter(price__range=(searchnumber, 10000))
        return render(request, "purchaser/purchaserhomepage.html", {"products": product})


def searchcategory(request):
    searchForm = request.POST
    searchText = searchForm["categorybar"]
    product = products.objects.filter(category__contains=searchText)

    return render(request, "purchaser/purchaserhomepage.html", {"products": product})

@login_required
def addComment(request,product_id):
    if request.method=='GET':
        myProduct = products.objects.get(id=product_id)
        return render(request, "purchaser/productDetails.html", {"product": myProduct})
    else:
        myProduct = products.objects.get(id=product_id)
        newComment=request.POST
        ncomment=newComment["comment"]
        mycomment = feedback( comment=ncomment, product=myProduct,barcode=myProduct.barcode)
        mycomment.save()
        return redirect("http://127.0.0.1:8000/purchaser/details/"+product_id)


def rating(request , product_id):

    total=0
    count=0
    ratingForm = request.POST
    ratingvalue = ratingForm["rating"]
    p=products.objects.get(id=product_id)
    p.rating=p.rating+ratingvalue
    strs=p.rating
    for i in range(1, len(strs)):
       total=total+ int(strs[i])
       count=count+1


    p.is_favorite=total/count
    p.save()
    return redirect("http://127.0.0.1:8000/purchaser/details/" + product_id)



