from rest_framework import serializers
from .models import *
from django.contrib.auth.models import *

#model serializers 

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'primaryCategory']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        
            model = Product
            
            
            fields= ['mainimage', 'name', 'preview_text', 'detail_text', 'price']
            
            
        
            def create(self, validated_data):
                return Product.objects.create(**validated_data) 
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields =  ['mainimage', 'name','category', 'preview_text', 'detail_text', 'price']
        
        def create(self, validated_data):
                return Product.objects.create(**validated_data)  
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields =  ['mainimage', 'name','category', 'preview_text']
        
        def create(self, validated_data):
                return Product.objects.create(**validated_data)  