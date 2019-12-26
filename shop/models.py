from django.db import models


# Create your models here.


class Customer(models.Model):
    userName = models.CharField(max_length =30)
    email = models.EmailField()
    
    objects = models.Manager()

    def save_customer(self):
        self.save()
        
    @classmethod
    def get_customer(cls, id):
        customer = Customer.objects.get(user=id)
        return customer
    
#category model
    
class Category (models.Model):
    title = models.CharField(max_length=300)
    primaryCategory= models.BooleanField(default=False)
    
    def__str__(self):
        return self.title
    
  #Product Model
  
  class Product(models.model):
        mainimage=models.ImageField(upload_to='products/',blank=True)
        