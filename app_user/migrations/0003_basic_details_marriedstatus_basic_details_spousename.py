# Generated by Django 4.0.7 on 2022-12-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_basic_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_details',
            name='marriedstatus',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basic_details',
            name='spousename',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
