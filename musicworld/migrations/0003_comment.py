# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=1000)),
                ('article', models.ForeignKey(to='musicworld.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
