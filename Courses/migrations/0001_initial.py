# Generated by Django 3.2.9 on 2022-04-15 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phoneNo', models.CharField(blank=True, max_length=100)),
                ('branch', models.CharField(blank=True, max_length=100)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('posted_by', models.CharField(blank=True, max_length=100)),
                ('posted_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
                ('about_course', models.TextField(blank=True)),
                ('requirement', models.TextField(blank=True)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('duration', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('posted_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Diploma_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('posted_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
