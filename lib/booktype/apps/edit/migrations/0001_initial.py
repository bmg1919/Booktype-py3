# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editor', '0006_auto_20150913_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_id', models.CharField(unique=True, max_length=50, verbose_name='cid')),
                ('author', models.CharField(default='', max_length=50, verbose_name='author')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('content', models.TextField(default='', verbose_name='content')),
                ('text', models.TextField(default='', verbose_name='text')),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='status')),
                ('state', models.PositiveSmallIntegerField(default=0, verbose_name='state')),
                ('is_imported', models.BooleanField(default=False, verbose_name='is_imported')),
                ('stored_reference', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(verbose_name='chapter', to='editor.Chapter', on_delete=models.CASCADE)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='edit.Comment', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
