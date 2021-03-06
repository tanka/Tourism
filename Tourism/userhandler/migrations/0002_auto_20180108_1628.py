# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-08 10:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userhandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('passport', models.CharField(max_length=30)),
                ('dateOfArrival', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('sex', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tourName', models.CharField(blank=True, max_length=30)),
                ('dateOfArrival', models.DateField(blank=True, null=True)),
                ('noOfPeople', models.IntegerField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('bookedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userhandler.Tour'),
        ),
    ]
