# Generated by Django 3.1.3 on 2020-11-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_eventresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventresult',
            name='img',
            field=models.CharField(default='', max_length=2083, unique=True),
        ),
    ]
