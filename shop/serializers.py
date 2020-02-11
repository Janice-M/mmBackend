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
            def delete(self, request, pk):
        # Get object with this pk
                article = get_object_or_404(Article.objects.all(), pk=pk)
    article.delete()
    return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204   
    
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