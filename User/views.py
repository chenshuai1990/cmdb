#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect,JsonResponse
from models import User
import time
import hashlib
import re

# Create your views here.
def login(request):
    return render_to_response('userTemplate/login.html', locals())
'''
def register(request):
    return render_to_response('userTemplate/register.html', locals())
'''


# Create your views here.
def r404(request):
    return render_to_response("404.html",locals())

#登录
def userlogin(request):
    if request.method == "POST"  and request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        hash = hashlib.md5()
        hash.update(password)
        password = hash.hexdigest()
        error=''
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                response = HttpResponseRedirect("/index")
                response.set_cookie("username",username,600)
                request.session["username"] = username+time.strftime("%H:%M:%S")
                return response
            else:
                error = "用户名或密码错误."
                return render_to_response('userTemplate/login.html', locals())
        except:
            return HttpResponseRedirect("/user/login")
    else:
        return render_to_response('userTemplate/login.html',locals())

def userLogin(request):
    if request.method == "POST"  and request.POST:
        statue = {"valid":'error'}
        try:
            username = request.POST.get('user')
            passord = request.POST.get('passwd')
            hash = hashlib.md5()
            hash.update(passord)
            password = hash.hexdigest()
            user = User.objects.get(username=username)
            if user.password == password:
                response = HttpResponseRedirect("/index")
                response.set_cookie("username",username,600)
                request.session["username"] = username+time.strftime("%H:%M:%S")
                return response
            else:
                return HttpResponseRedirect("/user/login")
        except:
            return HttpResponseRedirect("/user/login")
    else:
        return render_to_response('userTemplate/login.html',locals())

#判断登录用户是否存在
def userValidLogin(request):
    if request.method == 'POST' and request.POST:
        statue = {"valid": 'error'}
        try:
            username = request.POST.get('user')
            object = User.objects.filter(username = username)
            if object:
                statue["valid"] = 'success'
        except:
            pass
        return JsonResponse(statue)
    else:
        return HttpResponseRedirect("/user/login")



#表单数合法性验证
def data_isvalid(username, password, again):
    flag_user = 0
    flag_password = 0
    if password != again:
        flag_password = 0
    else:
        if password == '':
            flag_password = 0
        elif len(password) < 3 or len(password) > 18:
            flag_password = 0
        elif not (re.match('^\S+$', password)):
            flag_password = 0
        else:
            flag_password = 1
            # 用户名验证
    if username == '':
        flag_user = 0
    elif re.match('^\d.*$', username):
        flag_user = 0
    elif len(username) < 3 or len(username) > 18:
        flag_user = 0
    elif not (re.match('^\w+$', username)):
        flag_user = 0
    elif not (re.match('^[a-zA-Z]\w*', username)):
        flag_user = 0
    else:
        flag_user = 1
    if flag_user == 1 and flag_password == 1:
        return True
    else:
        return False

#注册
def register(request):
    if request.method =="POST" and request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        again = request.POST["again"]
        if data_isvalid(username,password,again):
            hash = hashlib.md5()
            hash.update(password)
            password = hash.hexdigest()
            u = User()
            u.username = username
            u.password = password
            u.save()
            return HttpResponseRedirect("/user/login")
        else:
            return render_to_response('userTemplate/register.html', locals())
    else:
        return render_to_response('userTemplate/register.html',locals())

#判断注册用户是否存在
def userValid(request):
    if request.method == 'POST' and request.POST:
        statue = {"valid": 'succes'}
        try:
            username = request.POST.get('user')
            object = User.objects.filter(username = username)
            if object:
                statue["valid"] = 'error'
        except:
            pass
        return JsonResponse(statue)
    else:
        return HttpResponseRedirect("/user/register")







