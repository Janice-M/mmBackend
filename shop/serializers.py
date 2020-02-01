from rest_framework import serializers
from .models import Category, Product, Service

#model serializers 

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
        class Meta:
        model = Product
        fields = '__all__' 
        author_id = serializers.IntegerField()
        
        def create(self, validated_data):
        return Product.objects.create(**validated_data)    
class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
        
