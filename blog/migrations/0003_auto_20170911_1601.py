# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='aboutnow',
            field=models.TextField(),
        ),
    ]