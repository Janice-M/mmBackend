from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from shop.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
#getting all products

class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
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
        
        