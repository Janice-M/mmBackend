from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
''' end of importations '''

urlpatterns = [
    path('',views.index,name='index'),
]