# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-03 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200203_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
