# Generated by Django 4.0.7 on 2022-12-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0008_medicaldetails_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaldetails',
            name='condition',
        ),
        migrations.AddField(
            model_name='basic_details',
            name='patdieases',
            field=models.CharField(max_length=200, null=True),
        ),
    ]