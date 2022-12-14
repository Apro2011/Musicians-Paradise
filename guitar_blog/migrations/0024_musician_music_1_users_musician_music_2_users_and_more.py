# Generated by Django 4.0.5 on 2022-08-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0023_alter_musician_music_1_votes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='music_1_users',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_2_users',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_3_users',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='musician',
            name='music_1_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='musician',
            name='music_2_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='musician',
            name='music_3_votes',
            field=models.IntegerField(default=0),
        ),
    ]
