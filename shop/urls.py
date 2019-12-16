from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views
''' end of importations '''

urlpatterns = [
    path('',views.index,name='index'),
    path('customer/',views.customer,name='customer'),
]