# Generated by Django 2.2 on 2019-12-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate_spots_app', '0004_auto_20191222_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='desc',
            field=models.TextField(),
        ),
    ]
