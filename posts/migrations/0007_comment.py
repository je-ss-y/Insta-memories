# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20191020_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Profile')),
            ],
        ),
    ]
