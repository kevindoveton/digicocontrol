# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SD9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aux1Values', models.CharField(max_length=255)),
                ('aux1Names', models.CharField(max_length=255)),
                ('aux2Values', models.CharField(max_length=255)),
                ('aux2Names', models.CharField(max_length=255)),
                ('aux3Values', models.CharField(max_length=255)),
                ('aux3Names', models.CharField(max_length=255)),
                ('aux4Values', models.CharField(max_length=255)),
                ('aux4Names', models.CharField(max_length=255)),
                ('aux5Values', models.CharField(max_length=255)),
                ('aux5Names', models.CharField(max_length=255)),
                ('aux6Values', models.CharField(max_length=255)),
                ('aux6Names', models.CharField(max_length=255)),
                ('aux7Values', models.CharField(max_length=255)),
                ('aux7Names', models.CharField(max_length=255)),
                ('aux8Values', models.CharField(max_length=255)),
                ('aux8Names', models.CharField(max_length=255)),
                ('aux9Values', models.CharField(max_length=255)),
                ('aux9Names', models.CharField(max_length=255)),
                ('aux10Values', models.CharField(max_length=255)),
                ('aux10Names', models.CharField(max_length=255)),
                ('aux11Values', models.CharField(max_length=255)),
                ('aux11Names', models.CharField(max_length=255)),
                ('aux12Values', models.CharField(max_length=255)),
                ('aux12Names', models.CharField(max_length=255)),
            ],
        ),
    ]
