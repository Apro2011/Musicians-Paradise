# Generated by Django 4.0.5 on 2022-08-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0026_remove_musician_music_1_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='music_1_votes',
            field=models.IntegerField(default=0),
        ),
    ]
