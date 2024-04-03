# Generated by Django 4.2.11 on 2024-03-07 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0005_alter_templeinfo_model_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='priest_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Address', models.TextField(max_length=30)),
                ('Jobtype', models.CharField(max_length=30)),
                ('Phone', models.BigIntegerField()),
                ('Email', models.EmailField(blank=True, max_length=254, verbose_name='Email Id')),
                ('Experience', models.IntegerField()),
                ('loc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.location_model')),
            ],
            options={
                'db_table': 'hindu_priest',
            },
        ),
    ]
