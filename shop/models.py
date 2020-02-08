from django.db import models


# Create your models here.



#category model
class Category (models.Model):
    title = models.CharField(max_length=300)
    primaryCategory= models.BooleanField(default=False)
    
    def __str__ (self):
        return self.title
    
#Product Model
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

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


        
class car(models.Model):
    
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