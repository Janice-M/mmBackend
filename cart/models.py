from django.db import models
from shop.models import *
# Create your models here.


#Get the customer model

Customer=get_customer_model()

#Cart

class Cart(models.Model):
    