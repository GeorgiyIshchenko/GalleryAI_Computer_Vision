# Generated by Django 3.2 on 2022-12-30 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20221124_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='threshold',
            field=models.IntegerField(blank=True, default=50, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
