# Generated by Django 3.1.7 on 2021-04-30 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanagedata', '0003_auto_20210430_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newregistration',
            old_name='image',
            new_name='userimages',
        ),
    ]