# Generated by Django 4.2.11 on 2024-03-08 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0006_priest_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='devoteereg_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=7)),
                ('photo', models.FileField(blank=True, upload_to='photos')),
                ('star', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email Id')),
                ('mobile', models.BigIntegerField()),
                ('loc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.location_model')),
            ],
            options={
                'db_table': 'devotee_reg',
            },
        ),
    ]
