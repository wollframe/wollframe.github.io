from django.forms import ModelForm
from django import forms

from .models import *

class Cl(forms.Form):
    km = forms.IntegerField()


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ("name","phone_number","departure", "arrival", "distance", "content")    
