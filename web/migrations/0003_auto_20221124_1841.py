# Generated by Django 3.2 on 2022-11-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20220920_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='device_path',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='device_uri',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
