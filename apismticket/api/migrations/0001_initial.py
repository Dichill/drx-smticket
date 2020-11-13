# Generated by Django 3.1.3 on 2020-11-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_location', models.CharField(default='', max_length=2083, unique=True)),
                ('movie_title', models.CharField(max_length=100)),
                ('movie_link', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
    ]