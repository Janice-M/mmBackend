from django.db import models
from shop.models import *
# Create your models here.


#Get the customer model

Customer=get_customer_model()

#Cart

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.quantity} of {self.item.name}'
    
    
#ordering after adding to cart model

class Order(models.Model):
    orderItems  = models.ManyToManyField(Cart)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username