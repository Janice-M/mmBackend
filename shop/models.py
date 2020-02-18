from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


#this user class inherits from django contrib fields

class User(User):
    
    pass




class Category (models.Model):
    title = models.CharField(max_length=300)
    primaryCategory= models.BooleanField(default=False)
    
    def __str__ (self):
        return self.title



class Product(models.Model):
    
    mainimage=models.ImageField(upload_to='products/',blank=True)
    name= models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name = 'Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name ='Detail Text')
    price = models.FloatField()
        
        
    def __str__(self):
        return self.name


        
class Car(models.Model):
    
    mainimage=models.ImageField(upload_to='products/',blank=True)
    name= models.CharField(max_length=300)
    slug = models.SlugField()
    parts= models.CharField(max_length=300)
    preview_text = models.TextField(max_length=200, verbose_name = 'Preview Text')
    
    def __str__(self):
        return self.name
    
    
        
    


class Service(models.Model):
    mainimage=models.ImageField(upload_to='services/',blank=True)
    name= models.CharField(max_length=300)
    slug = models.SlugField()
    preview_text = models.TextField(max_length=200, verbose_name = 'Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name ='Detail Text')
    price = models.FloatField()
        
        
    def __str__(self):
        return self.name