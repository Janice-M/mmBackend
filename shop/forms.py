
from django import forms
from .models import *

class newCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        
        fields = ('userName', 'email')