# Generated by Django 2.2 on 2019-12-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate_spots_app', '0002_auto_20191221_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='desc',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
