# Generated by Django 4.0.5 on 2023-05-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yoga_App', '0021_yogatable_contraindications'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasetable',
            name='video',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]