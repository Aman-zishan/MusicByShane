# Generated by Django 3.1 on 2020-08-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]