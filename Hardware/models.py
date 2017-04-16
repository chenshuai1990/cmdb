#coding:utf-8
from django.db import models

# Create your models here.
class Servers(models.Model):
    hostname = models.CharField(max_length = 32,verbose_name = "主机名")
    ip = models.CharField(max_length = 32,verbose_name = "ip")
    Mac = models.CharField(max_length = 32,verbose_name = "物理地址")
    cpu = models.CharField(max_length = 32,verbose_name = "cpu")
    Mem = models.CharField(max_length = 32,verbose_name = "内存")
    Disk = models.CharField(max_length = 32,verbose_name = "磁盘")
    system = models.CharField(max_length = 32,verbose_name = "系统")
    IO = models.CharField(max_length = 32,verbose_name = "IO")
    lastLogin = models.DateTimeField(verbose_name = "上次登录时间",blank=True)
    lastLoginUser = models.CharField(max_length=32,verbose_name = "上次登录用户",blank=True)
    isActive = models.CharField(max_length = 32,verbose_name = "是否被激活")



class Equipment(models.Model):
    ip = models.CharField(max_length=32,verbose_name="IP")
    uname = models.CharField(max_length=32,verbose_name="管理员账户")
    passwd= models.CharField(max_length=32,verbose_name="账户密码")