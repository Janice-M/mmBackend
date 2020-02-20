from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from shop.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#creating a user

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


class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
    
    # this is the api view methods for products
    
    
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
        pk = self.kwargs.get('pk')
        product.delete()
        return Response({"message": "Product with id `{}` has been deleted.".format(pk)},status=204)
    
    # # this is the api view methods for services
    
class ServiceView(APIView):
    
    def get(self, request):
        services = Service.objects.all()
        return Response({"services": services})
    #service post method
    def post(self, request):
            service = request.data.get('service')

        # Create a service on mech from the above data
            serializer = ServiceSerializer(data=service)
            if serializer.is_valid(raise_exception=True):
                service_saved = serializer.save()
            return Response({"success": "Service '{}' created successfully".format(service_saved.name)})
    #this delete method does not work and that is fine
    def delete(self, request, pk):
        # Get object 
        service = get_object_or_404(Service.objects.all(), pk=pk)
        pk = self.kwargs.get('pk')
        service.delete()
        return Response({"message": "Service with id `{}` has been deleted.".format(pk)},status=204)
    
class CarView(APIView):
    def get(self, request):
        services = Car.objects.all()
        return Response({"services": services})
        
        