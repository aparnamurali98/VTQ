# Generated by Django 4.2.11 on 2024-03-12 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0015_expense_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='poojaschedule_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timings', models.DateTimeField(max_length=8)),
                ('dayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.day_model')),
                ('poojaid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.pooja_model')),
            ],
            options={
                'db_table': 'pooja_schedule',
            },
        ),
    ]
