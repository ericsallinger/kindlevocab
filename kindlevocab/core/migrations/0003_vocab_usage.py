# Generated by Django 3.0.9 on 2020-08-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200813_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocab',
            name='usage',
            field=models.CharField(default='undefined', max_length=2000, verbose_name='Context'),
        ),
    ]
