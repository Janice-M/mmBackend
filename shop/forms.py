
from django import forms
from .models import *

class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']