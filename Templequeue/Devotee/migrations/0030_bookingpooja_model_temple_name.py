# Generated by Django 4.2 on 2025-02-27 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0066_staff_model_temple_name'),
        ('Devotee', '0029_alter_poojabook_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingpooja_model',
            name='Temple_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminhome.templeinfo_model'),
        ),
    ]
