# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('custom', models.TextField(default='{}', verbose_name='custom')),
                ('active', models.CharField(default='custom', max_length=32, verbose_name='active')),
                ('book', models.ForeignKey(verbose_name='book', to='editor.Book', on_delete=models.CASCADE)),
                ('owner', models.ForeignKey(default=None, verbose_name='owner', to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
