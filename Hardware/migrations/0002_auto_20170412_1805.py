# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hardware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='lastLoginUser',
            field=models.CharField(max_length=32, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7', blank=True),
        ),
    ]
