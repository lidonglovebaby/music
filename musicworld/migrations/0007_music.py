# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0006_pcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='music-title', max_length=200)),
                ('artist', models.CharField(verbose_name='music-artist', max_length=200)),
                ('album', models.CharField(verbose_name='music-album', max_length=200)),
                ('musicimage', models.FileField(upload_to='image/musics', verbose_name='music-image')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('music', models.FileField(upload_to='music/musics', verbose_name='musicM')),
                ('periodical', models.ForeignKey(to='musicworld.Periodical')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
