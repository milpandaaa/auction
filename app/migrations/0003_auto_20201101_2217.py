# Generated by Django 3.1.2 on 2020-11-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201101_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='cost',
            field=models.FloatField(),
        ),
    ]