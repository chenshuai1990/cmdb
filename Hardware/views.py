from django.shortcuts import render_to_response

# Create your views here.
def hardwarelist(request):
    return render_to_response('hardwareTemplate/hardwarelist.html', locals())

def management(request):
    return render_to_response('hardwareTemplate/management.html', locals())


