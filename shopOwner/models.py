from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
import django.contrib.auth
# Create your models here.
class requests(models.Model):
    name=models.CharField(max_length=250)
    category=models.CharField(max_length=300)
    numberOfItems=models.CharField(max_length=11)
    price=models.CharField(max_length=9)
    desc=models.CharField(max_length=500)

    barcode=models.PositiveIntegerField(default=0)
    requestOwner=models.ForeignKey(User,default=0)
    class Meta:
        permissions = (("can_add_request", "Send request"),("can_view_request","view request"))

class RequestForm(ModelForm):
    class Meta:
        model=requests
        fields=['name','category','numberOfItems','price','desc','barcode','requestOwner']


class SignUppForm(UserCreationForm ):
    email_address=forms.CharField(max_length=250 , required=True , widget=forms.EmailInput())
    type=forms.CharField(max_length=250,empty_value='owner')


    # address=forms.CharField(max_length=250)
    #number=forms.CharField(max_length=250)
    class Meta:
        model=User
        fields=('username','email_address','type','password1','password2')


class Student(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=300)
    mobile_number=models.CharField(max_length=11)
    academic_year=models.CharField(max_length=9)
class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=['name','address','mobile_number','academic_year']

