from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=250)
    category=models.CharField(max_length=300)
    price=models.PositiveIntegerField()
    numberOfItems=models.PositiveIntegerField()
    barcode=models.PositiveIntegerField(default=0)
    desc=models.CharField(max_length=500)
    status=models.BooleanField()
    owner=models.ForeignKey(User , default=0)

class itemForm(ModelForm):
    class Meta:
        model=items
        fields=['name','category','price','desc','status','numberOfItems','barcode' , 'owner']


