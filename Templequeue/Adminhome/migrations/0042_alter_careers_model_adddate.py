# Generated by Django 4.2.11 on 2024-04-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0041_alter_careers_model_adddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers_model',
            name='adddate',
            field=models.DateTimeField(max_length=10),
        ),
    ]
