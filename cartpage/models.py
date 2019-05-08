from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class cartproducts(models.Model):
    name=models.CharField(max_length=250)
    price=models.PositiveIntegerField("price")
    barcode=models.PositiveIntegerField(default=0)
    cartOwner=models.ForeignKey(User,default=0)

class cartproductForm(ModelForm):
    class Meta:
        model=cartproducts
        fields=['name','price','barcode','cartOwner']

