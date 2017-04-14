#coding:utf-8
from django.shortcuts import render_to_response
from mycmdb.views import *
from models import *
import datetime
from django.http import JsonResponse
from sshequipment import *

# Create your views here.
#==============硬件信息展示=======================



#查看设备列表
@user_valid
def hardwarelist(request):
    serverData = Servers.objects.all()
    return render_to_response('hardwareTemplate/hardwarelist.html', locals())

#新增硬件设备
@user_valid
def addserver(request):
    if request.method == 'POST' and request.POST:
        s = Servers()
        s.hostname = request.POST["HostName"]
        s.ip = request.POST["Ip"]
        s.Mac = request.POST["MAC"]
        s.cpu = request.POST["CPU"]
        s.Mem = request.POST["MEM"]
        s.Disk = request.POST["DISK"]
        s.system = request.POST["System"]
        s.IO = request.POST["IO"]
        s.lastLogin = datetime.datetime.now()
        # s.lastLoginUser = request.POST["LastLoginUser"]
        s.isActive = "N"
        s.save()
        return HttpResponseRedirect('/hardware/hardwarelist')
    else:
        return render_to_response('hardwareTemplate/addserver.html', locals())


#删除硬件设备
@user_valid
def delServer(request):
    if request.method == "POST" and request.POST:
        id = int(request.POST["id"])
        server = Servers.objects.get(id = id)
        server.delete()
        return JsonResponse({"statue":"success"})
    else:
        return JsonResponse({"statue":"error"})


#编辑硬件设备
@user_valid
def editServer(request,sid):
    Sid = int(sid)
    serverdata = Servers.objects.get(id=Sid)
    return render_to_response('hardwareTemplate/editserver.html',locals())




#远程服务器通过该接口传递硬件列表信息数据到数据库
def savedata(request):
    if request.method == "POST" and request.POST:
        host = request.POST["host"]
        ip = request.POST["ip"]
        mac = request.POST["mac"]
        cpu = request.POST["cpu"]
        mem = request.POST["mem"]
        fdisk = request.POST["fdisk"]
        osy = request.POST["os"]
        io = request.POST["io"]
        lastlogin = request.POST["lasttime"]
        lastuser = request.POST["lastuser"]
        isactive = "T"
        serverdata = Servers()
        serverdata.hostname = host
        serverdata.ip = ip
        serverdata.Mac = mac
        serverdata.cpu = cpu
        serverdata.Mem = mem
        serverdata.Disk = fdisk
        serverdata.system = osy
        serverdata.IO = io
        serverdata.lastLogin = datetime.datetime.now()
        serverdata.lastLoginUser = lastuser
        serverdata.isActive = isactive
        serverdata.save()
        result = {"statue":"success"}
    else:
        result = {"statue":"error"}
    return JsonResponse(result)


def getdata(request):
    result = {"statue":""}
    if request.method == "POST" and  request.POST:
        sid = request.POST.get("id")
        Sid = int(sid)
        s = Servers.objects.get(id = Sid)
        sip = s.ip
        result["statue"] = "success"
    else:
        result["statue"] = "fail"
    return  JsonResponse(result)

#=========================硬件远程管理===================================

#远程控制页面
@user_valid
def management(request):
    return render_to_response('hardwareTemplate/management.html', locals())



def doCommand(request):
    if request.method == "POST" and request.POST:
        command = request.POST.get("command")
        global m
        if m:
            result = m.docommand(command) #调用我们写好的执行方法
        else:
            result = "error"
        return JsonResponse({'result':result})# 这个返回值是在if判断成立以后执行的
    return JsonResponse({"name":"cindy"}) #是if判断失败执行的

m = None #定义一个全局变量 m 值为None
def login(request):
    if request.method == "POST" and request.POST:
        ip = request.POST["host"]
        user = request.POST["user"]
        password = request.POST["passwd"]

        global m #声明在函数当中使用和修改的是全局的m
        try:
            m = MyClient(ip,user,password)
            statue = "success"
        except Exception as e:
            m = None
            statue = "error"
    else:
        statue = "not fond"
    return JsonResponse({"statue":statue})

def logout(request):
    global m
    if m:
        del m
        statue = "退出成功"
        m = None
    else:
        statue =  "已经退出"
    return JsonResponse({"statue":statue})


