# Generated by Django 4.2 on 2025-03-05 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0010_devotee_model_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devotee_model',
            name='District',
        ),
    ]
