# Generated by Django 4.0.1 on 2022-05-02 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='tempuser',
        ),
    ]
