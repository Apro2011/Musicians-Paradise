# Generated by Django 4.0.5 on 2022-07-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0009_rename_musiciansongs_musiciansong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiciansong',
            name='music',
            field=models.FileField(default=None, upload_to='music/'),
        ),
    ]
