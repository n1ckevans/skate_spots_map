# Generated by Django 2.2 on 2019-12-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate_spots_app', '0003_marker_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
