# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaser', '0006_auto_20180205_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('payment_method', models.CharField(default=0, max_length=50)),
                ('telephoneNumber', models.PositiveIntegerField(default=0)),
                ('purchaser_id', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]