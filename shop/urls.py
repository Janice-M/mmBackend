from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from . views import ProductView,ServiceView, CarView
# from cart.views import add_to_cart, remove_from_cart


''' end of importations '''
#app name
app_name='products'


urlpatterns = [
    path('products/', ProductView.as_view()),
    url(r'api/users^$', views.UserCreate.as_view(), name='account-create'),
    path('services/', ServiceView.as_view()),
    path('cars/', CarView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls'))
]