from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views
''' end of importations '''

urlpatterns = [
    path('',views.register,name='register'),

]