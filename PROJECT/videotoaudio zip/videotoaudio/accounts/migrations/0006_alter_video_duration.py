# Generated by Django 4.1.5 on 2023-06-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_video_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.CharField(blank=True, default='00:00:00', max_length=8),
        ),
    ]