# Generated by Django 4.2.11 on 2024-05-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devotee', '0018_alter_payment_model_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_model',
            name='Total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
