# Generated by Django 3.1.8 on 2025-06-17 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20250616_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='creator',
        ),
    ]
