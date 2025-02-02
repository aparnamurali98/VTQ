# Generated by Django 4.2.11 on 2024-10-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminhome', '0056_templeinfo_model_pooja'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careers_model',
            old_name='adddate',
            new_name='Adddate',
        ),
        migrations.RemoveField(
            model_name='careers_model',
            name='notifyfile',
        ),
        migrations.AddField(
            model_name='careers_model',
            name='Notification_file',
            field=models.FileField(blank=True, upload_to='photos'),
        ),
    ]
