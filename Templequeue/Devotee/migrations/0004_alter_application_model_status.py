# Generated by Django 4.2.11 on 2024-04-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devotee', '0003_alter_application_model_application_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_model',
            name='Status',
            field=models.CharField(default='active', max_length=30),
        ),
    ]
