# Generated by Django 4.2 on 2023-05-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_rename_languages_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(to='MainApp.language'),
        ),
    ]
