# Generated by Django 4.1.5 on 2023-06-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_video_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
