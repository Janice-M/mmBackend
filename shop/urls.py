from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.authtoken import views
from django.urls import path, include
from . views import ProductView,ServiceView, CarView, UserCreate, LoginView
# from cart.views import add_to_cart, remove_from_cart


''' end of importations '''
#app name



urlpatterns = [
    path('products/', ProductView.as_view()),
    path('user/', UserCreate.as_view(), name='abc'),
    path('services/', ServiceView.as_view()),
    path('cars/', CarView.as_view()),
    
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    
    url(r'^get-user-auth-token/', views.obtain_auth_token, name='get_user_auth_token')
]