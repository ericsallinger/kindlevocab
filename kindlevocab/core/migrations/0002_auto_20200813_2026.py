# Generated by Django 3.0.9 on 2020-08-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocab',
            name='created',
        ),
        migrations.RemoveField(
            model_name='vocab',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='vocab',
            name='name',
        ),
        migrations.AddField(
            model_name='vocab',
            name='word',
            field=models.CharField(default='undefined', max_length=255, verbose_name='Word'),
        ),
    ]
