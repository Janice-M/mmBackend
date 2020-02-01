from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from . views import Home



''' end of importations '''
#app name
app_name='mainapp'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    
]