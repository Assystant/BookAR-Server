# Generated by Django 3.1.7 on 2021-04-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0015_auto_20210409_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='book_cover',
            field=models.ImageField(blank=True, default='placeholder_cover.png', null=True, upload_to='Book_Cover/'),
        ),
    ]
