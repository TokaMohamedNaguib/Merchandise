# Generated by Django 2.0 on 2018-02-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopOwner', '0007_requests_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='image',
        ),
        migrations.AlterField(
            model_name='requests',
            name='numberOfItems',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='requests',
            name='price',
            field=models.CharField(max_length=9),
        ),
    ]