from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import *
from .forms import *

# Create your views here.

def register(request):
    
    '''
    view function for registering a new customer
    '''
    if request.method=='POST':
        form=newCustomerForm(request.POST)

        
    else:
        form=newCustomerForm()

    return render(request,'registration/registration_form.html',{'form':form})
