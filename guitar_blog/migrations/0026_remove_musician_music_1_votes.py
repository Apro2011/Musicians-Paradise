# Generated by Django 4.0.5 on 2022-08-10 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0025_alter_musician_music_1_users_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='music_1_votes',
        ),
    ]
