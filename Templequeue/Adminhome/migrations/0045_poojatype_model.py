# Generated by Django 4.2.11 on 2024-04-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0044_alter_careers_model_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='poojatype_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pooja_type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'poojaTypecategory_model',
            },
        ),
    ]
