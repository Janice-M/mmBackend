from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from . import views
''' end of importations '''

urlpatterns = [
    path('',Home.as_view().name='home'),
    
]