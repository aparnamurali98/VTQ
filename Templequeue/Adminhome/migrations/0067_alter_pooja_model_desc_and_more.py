# Generated by Django 4.2 on 2025-02-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0066_staff_model_temple_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pooja_model',
            name='desc',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='templeinfo_model',
            name='discription',
            field=models.TextField(max_length=1000),
        ),
    ]
