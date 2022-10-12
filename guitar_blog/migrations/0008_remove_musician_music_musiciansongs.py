# Generated by Django 4.0.5 on 2022-07-05 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0007_alter_musician_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='music',
        ),
        migrations.CreateModel(
            name='MusicianSongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.FileField(blank=True, null=True, upload_to='music/')),
                ('by_musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitar_blog.musician')),
            ],
        ),
    ]