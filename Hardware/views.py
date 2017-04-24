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
    username = request.COOKIES["username"]
    serverData = Servers.objects.all()
    return render_to_response('hardwareTemplate/hardwarelist.html', locals())

#新增硬件设备
@user_valid
def addserver(request):
    username = request.COOKIES["username"]
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
    username = request.COOKIES["username"]
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
    username = request.COOKIES["username"]
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

#更新硬件信息
@user_valid
def getdata(request,sid):
    result = {"statue":""}
    try:
        if request.method == "POST" and  request.POST:
            sid = request.POST.get("id")   #从前端获取ID
            Sid = int(sid)
            s = Servers.objects.get(id = Sid)  #根据ID查找该设备的IP信息
            sip = s.ip
            eq = Equipment.objects.get(ip=sip)  #根据IP在设备登录表中查找账户密码信息
            ip = eq.ip
            usrname = eq.uname
            passwd = eq.passwd
            p = MyClient(ip,usrname,passwd)
            recv = p.updateserver(sid)
            if recv !="error":
                Recv = recv.splitlines()[:-1]
                Recv = eval(Recv[0])
                result["statue"] = Recv["statue"]
            else:
                result["statue"] = "error"
        else:
            result["statue"] = "error"
    except Exception as e:
        print e
    return  JsonResponse(result)

#远程传输数据的接口
def updatedata(request,sid):
    result = {"statue": ""}
    if request.method == "POST" and request.POST:
        Sid = int(sid)
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
        serverdata = Servers.objects.get(id = Sid)
        if serverdata.IO == io:
            result = {"statue":"no need to update"}
        else:
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
            result = {"statue": "success"}
    else:
        result = {"statue": "error"}
    return JsonResponse(result)



#=========================硬件远程操作==================================

#远程控制页面
@user_valid
def management(request):
    username = request.COOKIES["username"]
    return render_to_response('hardwareTemplate/management.html', locals())





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

@user_valid
def logout(request):
    global m
    if m:
        del m
        statue = "退出成功"
        m = None
    else:
        statue =  "已经退出"
    return JsonResponse({"statue":statue})


def doCommand(request):
    if request.method == "POST" and request.POST:
        command = request.POST.get("command")
        global m
        if m:
            result = m.docommand(command)#调用我们写好的执行方法
            Result = result[:-1]
            for i in range(len(Result)):
                Result[i] = Result[i].replace("01;34","")
                Result[i] = Result[i].replace("[0m", "")
            result = Result

        else:
            result = "error"
        return JsonResponse({'result':result})# 这个返回值是在if判断成立以后执行的
    return JsonResponse({"name":"cindy"}) #是if判断失败执行的








#=========================服务远程操作==================================
@user_valid
def operation(request,sid):
    username = request.COOKIES["username"]
    if sid=="all":
        S = Servers.objects.all()
    else:
        Sid = int(sid)
        S = Servers.objects.filter(id = Sid)
    C = Controlserver.objects.all()
    return render_to_response("hardwareTemplate/operation.html",locals())

def operationserver(request,sid,command):
    result={"statue":""}
    if request.method == "POST" and request.POST:
        Sid = int(sid)
        S = Servers.objects.get(id  =Sid)
        ip = S.ip
        Equip = Equipment.objects.get(ip=ip)
        username = Equip.uname
        password = Equip.passwd
        sername = request.POST["server"]
        p = MyClient(ip, username, password)
        recv = p.controlserver(Sid,sername,command)
        if recv !="error":
            Recv = recv.splitlines()[:-1]
            Recve = Recv[0]
            if Recve:
                result["statue"] = Recve
            else:
                result["statue"] = "Nothing"
        else:
            result["statue"] = "error"
    else:
        result["statue"] = "error"
    return JsonResponse(result)




#=========================磁盘清理==================================
def fdisk(request):
    return render_to_response("hardwareTemplate/fdisk.html")