# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-22 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ztour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.CharField(blank=True, max_length=255)),
                ('activate', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('document', models.FileField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_desc', models.CharField(blank=True, max_length=255)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ztour.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField()),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ztour.Image')),
            ],
        ),
        migrations.CreateModel(
            name='SmallImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('document', models.FileField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thumb_nail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ztour.SmallImage'),
        ),
        migrations.AddField(
            model_name='header',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ztour.Image'),
        ),
    ]
