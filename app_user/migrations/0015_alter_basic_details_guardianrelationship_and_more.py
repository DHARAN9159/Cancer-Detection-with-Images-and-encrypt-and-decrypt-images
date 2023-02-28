# Generated by Django 4.0.7 on 2023-01-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0014_alter_basic_details_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_details',
            name='guardianrelationship',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
