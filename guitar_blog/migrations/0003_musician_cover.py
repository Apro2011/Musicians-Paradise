# Generated by Django 4.0.5 on 2022-07-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0002_musician_appreciation'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='cover',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]