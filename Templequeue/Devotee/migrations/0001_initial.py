# Generated by Django 4.2.11 on 2024-04-18 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registration', '0007_alter_enquiry_model_query'),
        ('Adminhome', '0044_alter_careers_model_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='application_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resume', models.FileField(blank=True, upload_to='photos')),
                ('Status', models.CharField(default='Inactive', max_length=30)),
                ('Application_date', models.DateTimeField(max_length=10)),
                ('Devotee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.devotee_model')),
                ('careerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.careers_model')),
            ],
            options={
                'db_table': 'Application',
            },
        ),
    ]
