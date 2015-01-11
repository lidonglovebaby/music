# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0004_article_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('image', models.FileField(verbose_name='periodical-image', upload_to='image/periodical')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ptype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='periodical',
            name='ptype',
            field=models.ForeignKey(to='musicworld.Ptype'),
            preserve_default=True,
        ),
    ]
