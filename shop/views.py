from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import *
from .forms import *
from django.views.generic import ListView


# Create your views here.

""" @login_required(login_url='/accounts/login/') """

def register(request):
    
    '''
    view function for registering a new customer
    '''
    if request.method=='POST':
        form=newCustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            newCustomer = Customer(userName=userName, email=email) 
            recipient.save()
            HttpResponseRedirect('index')
    else:
        form=newCustomerForm()

    return render(request,'registration/registration_form.html',{'form':form})


#products view

class Home (ListView):
    