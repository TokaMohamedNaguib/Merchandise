# Create your views here.
from django.shortcuts import render,redirect
from shopOwner.models import requests,RequestForm
from .models import products,ProductForm
from systemAnalyst.models import itemForm,items
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required, user_passes_test


def group_required(*employee):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=employee)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)


#@permission_required('catalog.can_mark_returned')
@group_required('employees')
#show page of details of all items
def homeemployee(request):
    return render(request, "employee/employeehomepage.html",)

@group_required('employees')
def homeemployeeAdd(request):
    allproducts = items.objects.exclude(status=False)
    return render(request, "employee/shopowner.html", {"products": allproducts})

@group_required('employees')
def homeemployeeEdit(request):
    allproducts = products.objects.all()
    return render(request, "employee/purchaser.html", {"products": allproducts})


@group_required('employees')
#update item
def edit(request,product_id):
    if request.method=="GET":
        product = products.objects.get(id=product_id)
        return render(request, "employee/editProduct.html", {"product": product})
    else:
        old = products.objects.get(id=product_id)
        pr = ProductForm(request.POST)
        old.name = pr['name'].value()
        old.category = pr['category'].value()
        old.price = pr['price'].value()
        old.desc = pr['desc'].value()
        old.save()
        return redirect("listEdit")

@group_required('employees')
#add product to purchaser home page
def add(request,product_id):
    if request.method=='GET':
        product = items.objects.get(id=product_id)
        return render(request, "employee/Addproducts.html", {"product": product})
    else:
        pr=ProductForm(request.POST)
        pr.save()
        return redirect("listAdd")

@group_required('employees')
#delete item
def delete(request, product_id):
    products.objects.get(id=product_id).delete()
    return redirect("listEdit")

