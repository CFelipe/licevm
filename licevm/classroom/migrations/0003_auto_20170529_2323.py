# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20170529_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.Topic'),
        ),
    ]
