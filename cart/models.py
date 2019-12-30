from django.contrib.auth import get_user_model
from shop.models import Product
from django.db import models
# Create your models here.


#Get the customer model

User=get_user_model()

#Cart

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f'{self.quantity} of {self.item.name}'
    
    
#ordering after adding to cart model

class Order(models.Model):
    orderItems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username