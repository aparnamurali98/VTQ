# Generated by Django 4.2.11 on 2024-04-24 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0045_poojatype_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pooja_model',
            name='poojatypeid',
        ),
    ]
