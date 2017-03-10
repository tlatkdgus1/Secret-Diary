# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-10 07:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myMemo', '0005_remove_publicmemo_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicmemo',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
