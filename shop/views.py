from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import *
from .forms import *
from django.views.generic import ListView


# Create your views here.




#products view

class Home (ListView):
    model = Product
    template_name = 'products/home.html'