# Generated by Django 3.2.9 on 2022-04-14 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_mvp',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='listingDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]