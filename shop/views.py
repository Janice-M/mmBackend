from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from .models import *
from .serializers import *
#getting all products

class UserCreate(APIView):
    """ 
    Creating a user account
    """

    def post(self, request, format='json'):
        return Response('hello')
                        
class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})
    
    
    def post(self, request):
            product = request.data.get('product')

        # Create a product on mech from the above data
            serializer = ProductSerializer(data=product)
            if serializer.is_valid(raise_exception=True):
                product_saved = serializer.save()
            return Response({"success": "Product '{}' created successfully".format(product_saved.name)})
    
    def delete(self, request, pk):
        # Get object 
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"message": "Product with id `{}` has been deleted.".format(pk)},status=204)
    
    # get method for all services
    
class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        return Response({"services": services})
    
class CarView(APIView):
    def get(self, request):
        services = Car.objects.all()
        return Response({"services": services})
        
        