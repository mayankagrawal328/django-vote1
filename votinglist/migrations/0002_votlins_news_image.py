# Generated by Django 4.0.1 on 2022-05-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votinglist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votlins',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='logo/'),
        ),
    ]
