# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Controlserver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sname', models.CharField(max_length=32, verbose_name=b'mysql')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=32, verbose_name=b'IP')),
                ('uname', models.CharField(max_length=32, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe8\xb4\xa6\xe6\x88\xb7')),
                ('passwd', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.CharField(max_length=32, verbose_name=b'ip')),
                ('Mac', models.CharField(max_length=32, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x9c\xb0\xe5\x9d\x80')),
                ('cpu', models.CharField(max_length=32, verbose_name=b'cpu')),
                ('Mem', models.CharField(max_length=32, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('Disk', models.CharField(max_length=32, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98')),
                ('system', models.CharField(max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('IO', models.CharField(max_length=32, verbose_name=b'IO')),
                ('lastLogin', models.DateTimeField(verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('lastLoginUser', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7', blank=True)),
                ('isActive', models.CharField(max_length=32, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xa2\xab\xe6\xbf\x80\xe6\xb4\xbb')),
            ],
        ),
    ]
