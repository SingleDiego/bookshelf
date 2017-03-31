# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-27 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('publisher', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('ISBN', models.IntegerField(blank=True, null=True)),
                ('CLC', models.CharField(max_length=200, unique=True)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
