# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0009_auto_20150104_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodical',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
