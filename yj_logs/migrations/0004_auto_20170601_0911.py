# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yj_logs', '0003_auto_20170601_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '主题', 'verbose_name_plural': '主题'},
        ),
    ]
