# Generated by Django 3.1.7 on 2021-04-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0012_phrasesmodel_trigger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='Author_Image'),
        ),
    ]
