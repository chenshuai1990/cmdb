# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'T', max_length=4, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('realname', models.CharField(max_length=18, verbose_name=b'\xe7\x9c\x9f\xe5\xae\x9e\xe5\xa7\x93\xe5\x90\x8d', blank=True)),
                ('phone', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('email', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('role', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe8\xa7\x92\xe8\x89\xb2', blank=True)),
                ('comment', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('addtime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f', max_length=40)),
                ('gender', models.CharField(max_length=8, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', blank=True)),
                ('qq', models.CharField(max_length=18, verbose_name=b'QQ', blank=True)),
                ('status', models.CharField(default=b'T', max_length=4, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='User.BaseModel')),
                ('Name', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d')),
                ('description', models.TextField(verbose_name=b'\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            bases=('User.basemodel',),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='User.BaseModel')),
                ('Name', models.CharField(max_length=32, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.TextField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            bases=('User.basemodel',),
        ),
        migrations.CreateModel(
            name='Permission_Group',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='User.BaseModel')),
                ('PermissionId', models.IntegerField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90id')),
                ('groupId', models.IntegerField(verbose_name=b'\xe7\xbb\x84id')),
            ],
            bases=('User.basemodel',),
        ),
        migrations.CreateModel(
            name='User_Group',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='User.BaseModel')),
                ('userId', models.IntegerField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id')),
                ('groupId', models.IntegerField(verbose_name=b'\xe7\xbb\x84id')),
            ],
            bases=('User.basemodel',),
        ),
        migrations.CreateModel(
            name='User_Permission',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='User.BaseModel')),
                ('userId', models.IntegerField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id')),
                ('permissionId', models.IntegerField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90id')),
            ],
            bases=('User.basemodel',),
        ),
    ]
