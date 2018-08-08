# Generated by Django 2.0.3 on 2018-07-19 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20180719_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='slug',
            field=models.SlugField(max_length=500),
        ),
    ]
