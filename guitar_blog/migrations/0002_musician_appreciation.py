# Generated by Django 4.0.5 on 2022-07-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='appreciation',
            field=models.TextField(blank=True, null=True),
        ),
    ]