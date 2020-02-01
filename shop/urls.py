from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from . views import Home,Service
# from cart.views import add_to_cart, remove_from_cart


''' end of importations '''
#app name
app_name='mainapp'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('services/',Service.as_view(), name="service"),
    # path('cart/<slug>',add_to_cart, name='cart'),
    # path('remove/<slug>', remove_from_cart, name='remove-cart'),
]