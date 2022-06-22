from django import forms

class Product_form(forms.Form):
    name = forms.CharField(max_length=40)
    price = forms.IntegerField()
    description = forms.CharField(max_length=200)
    SKU = forms.CharField(max_length=30)
    active = forms.BooleanField()

class Category_form(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=200)

class Discount_form(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=40)
    price = forms.IntegerField()