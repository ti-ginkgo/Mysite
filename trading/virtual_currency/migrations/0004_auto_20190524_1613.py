# Generated by Django 2.2.1 on 2019-05-24 16:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_currency', '0003_auto_20190524_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='date',
        ),
        migrations.AddField(
            model_name='currency',
            name='saved_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 16, 13, 53, 983568, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='currencyhistory',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtual_currency.Currency'),
        ),
    ]
