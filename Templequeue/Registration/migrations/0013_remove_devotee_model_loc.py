# Generated by Django 4.2 on 2025-03-06 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0012_devotee_model_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devotee_model',
            name='loc',
        ),
    ]
