from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'login/',userlogin),
    url(r'register/',register),
    url(r'404',r404),
    url(r'userValid/',userValid),
    url(r'userLogin/',userValidLogin),


]