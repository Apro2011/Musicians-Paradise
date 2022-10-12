# Generated by Django 4.0.5 on 2022-07-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0016_remove_musician_music_remove_musician_music_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='music_1',
            field=models.FileField(default=None, upload_to='music/'),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_1_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_2',
            field=models.FileField(default=None, upload_to='music/'),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_2_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_3',
            field=models.FileField(default=None, upload_to='music/'),
        ),
        migrations.AddField(
            model_name='musician',
            name='music_3_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='MusicUpload',
        ),
    ]
