#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect,JsonResponse
from models import *
import time
import hashlib
import re
from mycmdb.views import *

# Create your views here.



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
            if user.password == password and user.status=='T':
                response = HttpResponseRedirect("/index")
                response.set_cookie("username",username,3600)
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

#登出
def logout(request):
    try:
        del request.COOKIES["username"]
        del request.session["username"]
    except:
        pass
    return HttpResponseRedirect("/user/login",locals())

#展示角色列表
@user_valid
def permissionPage(request):
    username = request.COOKIES["username"]
    p= Permission.objects.all()
    alldata = p
    return render_to_response('userTemplate/permission.html',locals())

#新增角色
@user_valid
def addpermission(request):
    username = request.COOKIES["username"]
    if request.method == "POST" and request.POST:
        name = request.POST["pername"]
        description = request.POST["description"]
        p = Permission(Name=name,description=description)
        # p.Name = name
        # p.description = description
        p.save()
        return HttpResponseRedirect('/user/permission/')
    else:
        return render_to_response("userTemplate/addpermission.html",locals())

#编辑角色
@user_valid
def editpermission(request):
    username = request.COOKIES["username"]
    return render_to_response('userTemplate/editpermission',locals())

#删除角色
@user_valid
def delpermission(request):
    username = request.COOKIES["username"]
    if request.method == "POST" and request.POST:
        id = int(request.POST["id"])
        p = Permission.objects.get(id = id)
        p.delete()
        return JsonResponse({"statue":"success"})
    else:
        return JsonResponse({"statue":"error"})

#查看个人信息
@user_valid
def personal(request):
    username = request.COOKIES["username"]
    u = User.objects.filter(username=username)
    alldata = u
    return render_to_response('userTemplate/personal.html',locals())

#查看用户列表
@user_valid
def userlist(request):
    username = request.COOKIES["username"]
    u = User.objects.all()
    alldata = u
    return render_to_response('userTemplate/userlist.html',locals())

#查看组列表
@user_valid
def usergroup(request):
    username = request.COOKIES["username"]
    return render_to_response('userTemplate/group.html',locals())