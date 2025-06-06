# Generated by Django 5.1.4 on 2025-06-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_faculty_cbf_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='cbadmin_id',
            field=models.CharField(default='CBAD001', editable=False, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='employee_id',
            field=models.CharField(default='J1098', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='admin_photos/'),
        ),
        migrations.AddField(
            model_name='admin',
            name='qualifications',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
