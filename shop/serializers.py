from rest_framework import serializers
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

#model serializers 

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

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
        fields =  ['mainimage','name','category', 'slug', 'preview_text']
        
        def create(self, validated_data):
                return Car.objects.create(**validated_data)  
            
            
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields =  ['product', 'service','preview_text', 'detail_text', 'price']
        
        def create(self, validated_data):
                return Package.objects.create(**validated_data)