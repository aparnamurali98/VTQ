# Generated by Django 4.2.11 on 2024-04-23 07:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Devotee', '0002_alter_application_model_application_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_model',
            name='Application_date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=10),
        ),
    ]
