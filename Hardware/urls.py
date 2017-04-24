from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'hardwarelist/',hardwarelist),
    url(r'management/',management),
    url(r'fdisk/', fdisk),
    url(r'addserver/',addserver),
    url(r'delserver/',delServer),
    url(r'savedata',savedata),
    url(r'editserver/(\d{1,2})',editServer),
    url(r'getdata/(\w{1,2})/',getdata),
    url(r'login/$',login),
    url(r'logout/$',logout),
    url(r'doCommand/',doCommand),
    url(r'updatedata/(\w{1,2})/',updatedata),
    url(r'operation/(\w{1,3})$',operation),
    url(r'operation/(\w{1,2})/(\w{4,6})', operationserver),

]


