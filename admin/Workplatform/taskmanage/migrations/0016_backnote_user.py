# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-01-11 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210106_1352'),
        ('taskmanage', '0015_note_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='backnote',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='修改用户'),
            preserve_default=False,
        ),
    ]