# Generated by Django 5.0.1 on 2024-01-05 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
    ]
