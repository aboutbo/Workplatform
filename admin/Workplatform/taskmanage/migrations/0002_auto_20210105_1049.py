# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-01-05 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notelog',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanage.Note', verbose_name='对应文件'),
        ),
    ]