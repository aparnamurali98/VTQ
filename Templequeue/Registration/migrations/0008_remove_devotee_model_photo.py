# Generated by Django 4.2 on 2025-02-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_alter_enquiry_model_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devotee_model',
            name='photo',
        ),
    ]
