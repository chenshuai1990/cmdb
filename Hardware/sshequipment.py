#coding:utf-8
import sys
import json
from django.http import JsonResponse
from django.shortcuts import render_to_response
import paramiko

class MyClient:
    def __init__(self,ip,user,password):
        # 登录到指定的服务器上
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.ssh.connect(
            hostname = ip,
            username = user,
            password = password
        )
        #在登录到的服务器上开启一个命令超时为2秒的交互式界面
        self.channel = self.ssh.invoke_shell()
        self.channel.settimeout(2)
    def docommand(self,command):
        command = "%s\n"%command #形成命令，\n代替了我们敲完命令之后的回车
        self.channel.send(command) #讲命令传到登录上的服务器上进行执行
        result_list = [] #定义一个空的列表用来存放结果
        while True: #死循环
            try: #为了捕获上面的timeout错误
                recv = self.channel.recv(99999) #接收我们服务器返回的结果
                recv = recv.strip().splitlines() #对接收到的内容首先去除多余的空格，然后进行以行切分
            except:
                recv = None #如果发生异常给recv一个值
            if isinstance(recv,str): #如果recv是字符串就放入列表
                result_list.append(recv)
            elif isinstance(recv,list): #如果recv是列表就和已有的结果列表进行拼接
                result_list += recv
            else:
                break
        result = "\n".join(result_list)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(result)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return result_list
        #
        # while recv:
        #     recv += self.channel.recv(99999)
        # return recv
    def __del__(self):
        self.channel.close() #关闭交互界面
        self.ssh.close() #关闭链接