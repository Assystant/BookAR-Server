# Generated by Django 3.1.7 on 2021-04-07 06:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0008_auto_20210407_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmodel',
            name='object',
            field=models.FileField(blank=True, null=True, upload_to='phrases_object/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['obj', 'fbx'])]),
        ),
    ]