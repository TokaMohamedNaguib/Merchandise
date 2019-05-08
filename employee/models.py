from django.db import models
from django.forms import ModelForm
# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=250)
    category=models.CharField(max_length=300)
    price=models.PositiveIntegerField("price")
    numberOfItems=models.PositiveIntegerField()
    desc=models.CharField(max_length=500)
    barcode=models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to="covers/%Y/%m/%D")
    is_favorite = models.IntegerField(default=1)
    rating = models.CharField(max_length=300, default="0")
class ProductForm(ModelForm):
    class Meta:
        model=products
        fields=['name','category','price','desc','numberOfItems','barcode','is_favorite','rating']
        permissions = (("can_mark_returned", "Set book as returned"),)

