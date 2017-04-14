from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'login/',userlogin),
    url(r'register/',register),
    url(r'404',r404),
    url(r'userValid/',userValid),
    url(r'userLogin/',userValidLogin),
    url(r'logout/$',logout),
    url(r'^permission/',permissionPage),
    url(r'addpermission/',addpermission),
    url(r'delpermission/',delpermission),
    url(r'personal/',personal),
    url(r'userlist/',userlist),
    url(r'group/',usergroup),




]