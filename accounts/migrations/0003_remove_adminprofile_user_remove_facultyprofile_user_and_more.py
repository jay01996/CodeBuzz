# Generated by Django 5.1.4 on 2025-05-26 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_adminprofile_email_adminprofile_full_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='facultyprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='user',
        ),
    ]
