# Generated by Django 3.1.7 on 2021-04-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0011_auto_20210407_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrasesmodel',
            name='trigger',
            field=models.ImageField(default='placeholder_cover.png', upload_to='trigger_image/'),
            preserve_default=False,
        ),
    ]
