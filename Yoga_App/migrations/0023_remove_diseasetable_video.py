# Generated by Django 4.0.5 on 2023-05-30 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Yoga_App', '0022_diseasetable_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasetable',
            name='video',
        ),
    ]
