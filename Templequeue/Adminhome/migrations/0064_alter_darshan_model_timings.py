# Generated by Django 4.2.11 on 2024-10-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0063_alter_darshan_model_timings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darshan_model',
            name='Timings',
            field=models.CharField(max_length=50),
        ),
    ]
