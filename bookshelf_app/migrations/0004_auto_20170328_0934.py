# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf_app', '0003_auto_20170328_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ISBN'),
        ),
    ]
