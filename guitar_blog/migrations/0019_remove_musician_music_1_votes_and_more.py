# Generated by Django 4.0.5 on 2022-08-01 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0018_musician_music_1_votes_musician_music_2_votes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='music_1_votes',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='music_2_votes',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='music_3_votes',
        ),
    ]
