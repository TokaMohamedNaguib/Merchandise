from django import forms



class contactform(forms.Form):
     # full_name=forms.CharField(required=False)
     email=forms.EmailField(required=False)
     # message=forms.CharField(required=False)

