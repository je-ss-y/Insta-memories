# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 12:22
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_image_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=tinymce.models.HTMLField(),
        ),
    ]