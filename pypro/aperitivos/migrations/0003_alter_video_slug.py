# Generated by Django 4.0.4 on 2022-05-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0002_video_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
    ]
