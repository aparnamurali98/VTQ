# Generated by Django 4.2.11 on 2024-04-29 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0049_pooja_model_photo'),
        ('Devotee', '0005_poojabook_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poojabook_model',
            name='pooja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.pooja_model', unique=True),
        ),
    ]
