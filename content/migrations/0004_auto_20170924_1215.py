# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 12:15
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='corpo',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]