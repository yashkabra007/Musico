# Generated by Django 2.1.5 on 2019-01-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file_type',
            field=models.CharField(default='mp3', max_length=10),
        ),
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
