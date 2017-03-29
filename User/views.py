from django.shortcuts import render_to_response

# Create your views here.
def login(request):
    return render_to_response('userTemplate/login.html', locals())

def register(request):
    return render_to_response('userTemplate/register.html', locals())