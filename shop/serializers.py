from rest_framework import serializers
from .models import Category, Product, Service

#model serializers 

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class productSerializer(serializers.ModelSerializer):
        class Meta:
        model = Product
        fields = '__all__'     
class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
        
