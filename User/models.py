#coding:utf-8
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    status = models.CharField(max_length=4, verbose_name='用户状态', default='T', blank=True)

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    realname = models.CharField(max_length=18, verbose_name='真实姓名', blank=True)
    phone = models.CharField(max_length=32, verbose_name='手机号码', blank=True)
    email = models.CharField(max_length=50, verbose_name='用户邮箱', blank=True)
    role = models.CharField(max_length=32, verbose_name='用户角色', blank=True)
    comment = models.TextField(verbose_name='备注', blank=True)
    addtime = models.DateTimeField(max_length=40, verbose_name='添加日期', auto_now=True)
    gender = models.CharField(max_length=8, verbose_name='性别', blank=True)
    qq = models.CharField(max_length=18, verbose_name='QQ', blank=True)
    status = models.CharField(max_length=4, verbose_name='用户状态', default='T', blank=True)

class Group(BaseModel):
    Name = models.CharField(max_length=32,verbose_name="组名")
    description = models.TextField(verbose_name="组描述")

class Permission(BaseModel):
    Name = models.CharField(max_length=32, verbose_name="权限名称")
    description = models.TextField(verbose_name="权限描述")

class User_Group(BaseModel):
    userId = models.IntegerField(verbose_name="用户id")
    groupId = models.IntegerField(verbose_name="组id")

class User_Permission(BaseModel):
    userId = models.IntegerField(verbose_name="用户id")
    permissionId = models.IntegerField(verbose_name="权限id")

class Permission_Group(BaseModel):
    PermissionId = models.IntegerField(verbose_name="权限id")
    groupId = models.IntegerField(verbose_name="组id")