from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Service

#getting all products

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({"products": products})
    
    # get method for all services
       
class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        return Response({"services": services})
        
        