# Generated by Django 4.2 on 2025-03-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0078_remove_templeinfo_model_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers_model',
            name='Notification',
            field=models.CharField(max_length=50),
        ),
    ]
