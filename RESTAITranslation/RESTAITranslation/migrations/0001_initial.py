# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('algorithmId', models.BigIntegerField()),
                ('algorithmName', models.CharField(default='', max_length=200)),
                ('algorithmDescription', models.TextField()),
            ],
            options={
                'ordering': ('algorithmId',),
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('originalText', models.TextField()),
                ('translatedText', models.TextField()),
                ('sourceLanguage', models.CharField(default='Chinese', max_length=200)),
                ('targetLanguage', models.CharField(default='English', max_length=200)),
                ('algorithmId', models.BigIntegerField()),
                ('algorithmName', models.CharField(default='', max_length=200)),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
