# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0008_userinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='article',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='periodical',
        ),
    ]
