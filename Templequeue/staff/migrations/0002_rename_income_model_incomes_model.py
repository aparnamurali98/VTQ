# Generated by Django 4.2.11 on 2024-05-09 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_alter_enquiry_model_query'),
        ('Devotee', '0021_alter_payment_model_total_amount'),
        ('Adminhome', '0050_remove_poojatype_model_photo'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='income_model',
            new_name='incomes_model',
        ),
    ]
