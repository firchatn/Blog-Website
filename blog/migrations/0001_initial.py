# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('aboutnow', models.CharField(max_length=3000)),
                ('img', models.ImageField(upload_to='upload/')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='upload/')),
                ('joind_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]