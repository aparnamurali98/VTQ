# Generated by Django 4.2 on 2025-03-08 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0077_templeinfo_model_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templeinfo_model',
            name='District',
        ),
    ]
