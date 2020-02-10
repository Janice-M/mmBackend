from rest_framework import serializers
from .models import Category, Product, Service

#model serializers 

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
        
            
            mainimage=serializers.ImageField()
            name= serializers.CharField(max_length=300)
            slug = serializers.SlugField()
            
            preview_text = serializers.CharField(max_length=200, verbose_name = 'Preview Text')
            detail_text = serializers.CharField(max_length=1000, verbose_name ='Detail Text')
            price = serialisers.CharField() 
            user_id = serializers.CharField()
        
            def create(self, validated_data):
                return Product.objects.create(**validated_data)    
    
class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
        
