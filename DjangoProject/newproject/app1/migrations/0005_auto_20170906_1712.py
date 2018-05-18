# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20170824_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='Name',
            new_name='name',
        ),
    ]
