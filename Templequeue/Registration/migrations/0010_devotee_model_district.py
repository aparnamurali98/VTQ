# Generated by Django 4.2 on 2025-03-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0077_templeinfo_model_district'),
        ('Registration', '0009_remove_devotee_model_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='devotee_model',
            name='District',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminhome.distric_model'),
        ),
    ]
