# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_rescate', models.DateField()),
            ],
        ),
    ]
