from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Service

#getting all products

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
        
    
    # get method for all services
       
class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        return Response({"services": services})
        
        