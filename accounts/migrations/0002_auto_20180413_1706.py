# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 17:06
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.user_directory_path),
        ),
    ]
