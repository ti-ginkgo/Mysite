# Generated by Django 2.2.1 on 2019-05-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='count',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='currency',
            name='volume',
            field=models.FloatField(default=0.0),
        ),
    ]
