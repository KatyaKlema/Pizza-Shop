from django.contrib.auth.models import User
from django import forms
from shopapp.models import Product

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

#class ShopForm(forms.ModelForm):
 #   class Meta:
  #      model = usr
   #     fields = ('name', 'phone', 'address')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'short_description', 'image', 'price')