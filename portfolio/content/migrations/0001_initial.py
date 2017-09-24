# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=50)),
                ('corpo', models.TextField()),
                ('data', models.DateField()),
                ('tag', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
    ]
