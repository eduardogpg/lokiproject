# Generated by Django 3.2.7 on 2021-09-25 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0003_wallet_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]