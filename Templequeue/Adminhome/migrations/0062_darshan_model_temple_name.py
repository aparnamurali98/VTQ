# Generated by Django 4.2.11 on 2024-10-07 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0061_specialday_model_temple_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='darshan_model',
            name='Temple_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminhome.templeinfo_model'),
        ),
    ]
