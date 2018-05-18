# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True)),
                ('teamLead', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('numberOfEmployees', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(to='app1.Department', default=1),
            preserve_default=False,
        ),
    ]
