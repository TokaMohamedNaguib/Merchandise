# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemAnalyst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='numberOfItems',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]