from  django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

import socket
socket.getaddrinfo('localhost', 8080)



from purchaser.models import payment,paymentForm

from purchaser.models import SignUpForm
from .models import User
from .forms import contactform

# Create your views here.
from django.shortcuts import render , redirect
from employee.models import products,ProductForm
from .models import cartproducts , cartproductForm
from django.views import generic
from django.views.generic import View

# Create your views here.

def homecart(request,user_id):
    total=0
    count=0
    cartOwner = User.objects.get(id=user_id)
    allProducts=cartproducts.objects.filter(cartOwner=cartOwner)
    for obj in cartproducts.objects.filter(cartOwner=cartOwner):
            total+=obj.price
            count += 1

    return render(request,"cartpage/cartpage.html",{"products":allProducts,"total":total,"count":count})

def delete(request,user_id, product_id):
    cartOwner = User.objects.get(id=user_id)
    count=0
    total=0
    myCart=cartproducts.objects.get(cartOwner=cartOwner,id=product_id)
    #deleteProduct = myCart.objects.get(id=product_id)
    bar=myCart.barcode
    myProduct = products.objects.get(barcode=bar)
    x = myProduct.numberOfItems + 1
    myProduct.numberOfItems =x
    myProduct.save()
    myCart.delete()
    allProducts=cartproducts.objects.filter(cartOwner=cartOwner)
    for obj in cartproducts.objects.filter(cartOwner=cartOwner):
            total+=obj.price
            count += 1
    return render(request, "cartpage/cartpage.html", {"products": allProducts, "total": total, "count": count})

def paymentdetails(request,user_id):
    if request.method=="GET":
        cartOwner = User.objects.get(id=user_id)
        count = 0
        total = 0
        newPayment = paymentForm()
        allProducts = cartproducts.objects.filter(cartOwner=cartOwner)
        for obj in cartproducts.objects.filter(cartOwner=cartOwner):
            total += obj.price
            count += 1
        if total==0:
            return render(request,"error.html")
        newPayment.purchaser_id = user_id
        return render(request, "paymentdetails.html", {"total":total})
    else:
        pay=paymentForm(request.POST)
        pay.save()

        cartowner = User.objects.get(id=user_id)

        form = contactform(request.POST or None)
        if form.is_valid():
            form_email = form.cleaned_data.get("email")
            form_message = form.cleaned_data.get("message")
            form_full_name = form.cleaned_data.get("full_name")

            subject = 'Mail from Merchandise'
            from_email = settings.EMAIL_HOST_USER
            to_email = [cartowner.email]
            contact_message = "%s: %s via %s" % (
                'Merchandise Team',
                'your product confirmed',
                form_email)

            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=False)

        context = {
            "form": form,
        }
        return render(request, "paymentdetails.html", context)
























