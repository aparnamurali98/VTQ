# Generated by Django 4.2.11 on 2024-03-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0014_month_model_alter_day_model_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='expense_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exptype', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Expense_type',
            },
        ),
    ]
