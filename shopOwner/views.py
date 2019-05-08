from django.shortcuts import render
from django.shortcuts import redirect
from .models import RequestForm , StudentForm,User
from .models import requests
from systemAnalyst.models import items,itemForm
from shopOwner.models import SignUppForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import user_passes_test

def group_required(*shopOwners):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=shopOwners)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)
# Create your views here.
@group_required('shopOwners')
def homeShopOwner(request):
    return  render(request,"shopOwner/homeShopOwner.html")

@group_required('shopOwners')
def requestPage(request):
    return render(request,"shopOwner/askForRequest.html")

def signUp (request):
    return render(request, "purchaser/signUp.html")


@group_required('shopOwners')
def create(request,user_id):
    if request.method=='GET':
        return render(request, "shopOwner/create.html")
    else:
        shopOwner = User.objects.get(id=user_id)
        newRequest = request.POST
        name = newRequest["name"]
        category = newRequest["category"]
        price = newRequest["price"]
        numberOfItems = newRequest["numberOfItems"]
        desc = newRequest["desc"]
        myRequest = requests(name=name,price=price,category=category,desc=desc,numberOfItems=numberOfItems, requestOwner=shopOwner)
        myRequest.save()
        return redirect('http://127.0.0.1:8000/shopOwner/%d' % shopOwner.id)

@group_required('shopOwners')
def index(request, user_id):
            shopOwner = User.objects.get(id=user_id)
            allrequest=items.objects.filter(owner=shopOwner)
            return render(request, "shopOwner/homeShopOwner.html", {"requests": allrequest})



def signUpp(request):
    if request.method=='POST':
        form=SignUppForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            group = Group.objects.get(name='shopOwners')
            user.groups.add(group)
            return redirect('http://127.0.0.1:8000/shopOwner/%d' %user.id )
    else:
        form=SignUppForm()
        return render(request,'shopOwner/signUpp.html',{'form':form})

