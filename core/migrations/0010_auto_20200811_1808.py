# Generated by Django 3.1 on 2020-08-11 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_gallery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Gallery_image',
        ),
    ]