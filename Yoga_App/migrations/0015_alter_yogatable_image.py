# Generated by Django 4.0.5 on 2023-05-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yoga_App', '0014_alter_yogatable_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yogatable',
            name='image',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
