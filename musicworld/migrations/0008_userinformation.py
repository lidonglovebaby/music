# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicworld', '0007_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinformation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('email', models.CharField(null=True, max_length=200)),
                ('hobby', models.CharField(null=True, max_length=200)),
                ('image', models.ImageField(null=True, verbose_name='user-image', upload_to='/image/userinformation')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(null=True, to='musicworld.Article')),
                ('periodical', models.ForeignKey(null=True, to='musicworld.Periodical')),
                ('user', models.OneToOneField(to='musicworld.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
