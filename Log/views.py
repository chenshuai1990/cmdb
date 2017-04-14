from django.shortcuts import render_to_response
from mycmdb.views import *
# Create your views here.

@user_valid
def index(request):
    return render_to_response('logTemplate/log.html', locals())