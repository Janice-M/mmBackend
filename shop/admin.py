from django.contrib import admin
from .models import Category, Product,Service, User
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(User)
