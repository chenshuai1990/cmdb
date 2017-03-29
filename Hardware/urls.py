from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'hardwarelist/',hardwarelist),
    url(r'management/',management)

]


