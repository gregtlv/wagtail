# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171227_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.TextField(),
        ),
    ]
