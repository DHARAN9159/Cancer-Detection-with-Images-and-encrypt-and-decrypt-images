# Generated by Django 4.0.7 on 2022-12-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0007_medicaldetails_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaldetails',
            name='condition',
            field=models.BooleanField(default=False),
        ),
    ]