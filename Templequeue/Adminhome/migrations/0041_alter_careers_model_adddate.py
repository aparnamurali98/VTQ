# Generated by Django 4.2.11 on 2024-04-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0040_alter_careers_model_adddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers_model',
            name='adddate',
            field=models.CharField(max_length=50),
        ),
    ]
