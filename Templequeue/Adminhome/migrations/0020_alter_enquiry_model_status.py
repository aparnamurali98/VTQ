# Generated by Django 4.2.11 on 2024-03-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0019_enquiry_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry_model',
            name='Status',
            field=models.CharField(default='inactive', max_length=50),
        ),
    ]
