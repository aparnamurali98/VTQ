# Generated by Django 4.2 on 2025-02-10 05:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Devotee', '0029_alter_poojabook_model_name'),
        ('Registration', '0007_alter_enquiry_model_query'),
        ('Adminhome', '0065_darshan_model_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='incomes_model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_date', models.DateTimeField(default=django.utils.timezone.now, max_length=10)),
                ('Amount', models.IntegerField()),
                ('Narration', models.TextField(max_length=30, null=True)),
                ('Bookingpooja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Devotee.bookingpooja_model')),
                ('Devotee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.devotee_model')),
                ('Temple_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminhome.templeinfo_model')),
                ('income_typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminhome.income_model')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminhome.staff_model')),
            ],
        ),
    ]
