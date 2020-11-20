from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Auction_form(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['product', 'count', 'cost', 'username', 'date']
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'count', 'cost', 'farm']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'farm': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Farm_form(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'address', 'phone_number', 'name_directors', 'phone_directors']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'name_directors': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_directors': forms.TextInput(attrs={'class': 'form-control'}),
        }
