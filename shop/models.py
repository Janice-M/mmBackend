from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import ArrayField


#begining od models
#Category model

class Category (models.Model):
    title = models.CharField(max_length=300)
    primaryCategory= models.BooleanField(default=False)

    def __str__ (self):
        return self.title




#produt/parts model

class Product(models.Model):

    mainimage=models.ImageField(upload_to='products/',blank=True)
    name= models.CharField(max_length=300)
    slug = models.SlugField(primary_key=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name = 'Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name ='Detail Text')
    price = models.FloatField()



    def __str__(self):
        return self.name

#services model

class Service(models.Model):

    mainimage=models.ImageField(upload_to='services/',blank=True)
    name= models.CharField(max_length=300)
    slug = models.SlugField(primary_key=True, unique=True)
    preview = models.TextField(max_length=200, verbose_name = 'Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name ='Detail Text')
    price = models.FloatField()


    def __str__(self):
        return self.name

#car(vehicle) model

class Car(models.Model):

    mainimage=models.ImageField(upload_to='cars/',blank=True)
    name= models.CharField(max_length=300)
    parts= models.CharField(max_length=300)
    preview_text = models.TextField(max_length=200, verbose_name = 'Preview Text')

    def __str__(self):
        return self.name

#this user class inherits from django contrib fields

class User(User):

    pass


#pakages model

class Package(models.Model):

    mainimage=models.ImageField(upload_to='packages/',blank=True)
    name= models.CharField(max_length=300, null=True)
    slug = models.SlugField(primary_key=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name = 'Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name ='Detail Text')
    price = models.FloatField(max_length=1000)

    def __str__(self):
        return self.name


class Order(models.Model):

    name = models.CharField(max_length=300, null=True)
    slug = models.SlugField(primary_key=True, unique=True)
    ordered_items = ArrayField(models.CharField(max_length=200))
    total_price = models.FloatField(max_length=1000)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
