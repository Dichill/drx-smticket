# Generated by Django 3.1.3 on 2020-11-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_eventresult_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventresult',
            name='img',
            field=models.CharField(max_length=2083),
        ),
        migrations.AlterField(
            model_name='eventresult',
            name='link',
            field=models.CharField(max_length=2083),
        ),
        migrations.AlterField(
            model_name='movieresult',
            name='link',
            field=models.CharField(max_length=2083),
        ),
    ]