from django.shortcuts import render_to_response
from mycmdb.views import *
import peewee

# Create your views here.

@user_valid
def index(request):
    return render_to_response('apiTemplate/api.html',locals())



def sshserver(request):
    pass