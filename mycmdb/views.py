#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

#定义判断用户seesion权限的装饰器
def user_valid(fun):
    def valid(request,*args,**kwargs):
        try:
            request.COOKIES["username"] and request.session["username"]
            username = request.COOKIES["username"]
            return fun(request,*args,**kwargs)
        except Exception,e:
            print e
            return HttpResponseRedirect("/user/login")
    return valid

#登录后跳转的首页，并使用装饰器判断cookie和seesion
@user_valid
def index(request):
    username = request.COOKIES["username"]
    return render_to_response('index.html',locals())