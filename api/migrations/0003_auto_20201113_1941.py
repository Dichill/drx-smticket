# Generated by Django 3.1.3 on 2020-11-13 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201113_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SearchResults',
            new_name='SearchResult',
        ),
    ]