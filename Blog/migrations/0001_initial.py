# Generated by Django 3.2.9 on 2022-04-15 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(blank=True, max_length=100)),
                ('header', models.CharField(blank=True, max_length=200)),
                ('header2', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('posted_by', models.CharField(blank=True, max_length=100)),
                ('posted_day', models.CharField(blank=True, max_length=100)),
                ('posted_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
                ('title2', models.CharField(blank=True, max_length=100)),
                ('more_blog', models.TextField(blank=True)),
                ('title3', models.CharField(blank=True, max_length=100)),
                ('article', models.TextField(blank=True)),
                ('article2', models.TextField(blank=True)),
                ('team', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('team_name', models.CharField(blank=True, max_length=100)),
                ('content', models.CharField(blank=True, max_length=100)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]