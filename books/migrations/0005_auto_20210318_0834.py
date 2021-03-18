# Generated by Django 3.1.7 on 2021-03-18 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210317_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrasesmodel',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phrases', to='books.bookmodel'),
        ),
    ]
