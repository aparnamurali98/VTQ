# Generated by Django 4.2.11 on 2024-03-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0006_alter_enquiry_model_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry_model',
            name='Query',
            field=models.TextField(max_length=200),
        ),
    ]
