# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0005_auto_20150104_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=1000)),
                ('periodical', models.ForeignKey(to='musicworld.Periodical')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
