# Generated by Django 3.1.7 on 2021-03-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0003_auto_20210325_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authormodel',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='authormodel',
            name='about',
        ),
        migrations.RemoveField(
            model_name='authormodel',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='authormodel',
            name='death_date',
        ),
        migrations.AddField(
            model_name='authormodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
