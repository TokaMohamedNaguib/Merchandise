from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import ModelForm
from employee.models import products
import django.contrib.auth


class SignUpForm(UserCreationForm):
    email=forms.EmailField( required=True,widget=forms.EmailInput)

    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class feedback(models.Model):
    comment=models.CharField(max_length=1000)
    product=models.ForeignKey(products,related_name='feedbacks',default=0)
    barcode=models.PositiveIntegerField(default=0)
    #created_at=models.DateTimeField(auto_now_add=True)

class feedbackForm(ModelForm):
    class Meta:
        model=feedback
        fields=['comment','product','barcode']

class payment(models.Model):
    address=models.CharField(max_length=1000,default=00)
    payment_method=models.CharField(max_length=50,default=0)
    country=models.CharField(max_length=50,default=0)
    telephoneNumber=models.PositiveIntegerField(default=0)
    #purchaser_id=models.PositiveIntegerField(default=0)

class paymentForm(ModelForm):
    class Meta:
        model=payment
        fields=['address','payment_method','country','telephoneNumber']

