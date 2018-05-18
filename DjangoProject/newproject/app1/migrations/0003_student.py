# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20170816_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('firstName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100)),
                ('RollNo', models.IntegerField(null=True)),
            ],
        ),
    ]
