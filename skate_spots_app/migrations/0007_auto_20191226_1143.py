# Generated by Django 2.2 on 2019-12-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate_spots_app', '0006_auto_20191222_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
