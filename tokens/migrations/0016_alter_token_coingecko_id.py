# Generated by Django 3.2.7 on 2021-10-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0015_token_coingecko_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='coingecko_id',
            field=models.CharField(max_length=100),
        ),
    ]