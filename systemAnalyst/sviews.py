from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from shopOwner.models import requests,RequestForm
from .models import items,itemForm
from employee.models import ProductForm


def group_required(*analyst):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=analyst)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)
# Create your views here.

@group_required('analysts')
#show page of details of all items
def home(request):
    allproducts = requests.objects.all()
    return render(request, "systemAnalyst/analystHomePage.html", {"products": allproducts})


#accept product
@group_required('analysts')
def accept(request,product_id):
    if request.method=='GET':
        product = requests.objects.get(id=product_id)
        return render(request, "systemAnalyst/acceptProduct.html", {"product": product})
    else:
        product = requests.objects.get(id=product_id)
        pr=items(status=True,name=product.name,category=product.category,price=product.price,desc=product.desc,barcode=product.barcode,owner=product.requestOwner,numberOfItems=product.numberOfItems)
        requests.objects.get(id=product_id).delete()
        pr.save()
        return redirect("analystlist")

@group_required('analysts')
#reject product
def reject(request,product_id):
    if request.method=='GET':
        product = requests.objects.get(id=product_id)
        return render(request, "systemAnalyst/rejectProduct.html", {"product": product})
    else:
        product = requests.objects.get(id=product_id)
        pr = items(status=False, name=product.name, category=product.category, price=product.price, desc=product.desc,
                   barcode=product.barcode, owner=product.requestOwner, numberOfItems=product.numberOfItems)
        requests.objects.get(id=product_id).delete()
        pr.save()
        return redirect("analystlist")




