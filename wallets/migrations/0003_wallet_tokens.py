# Generated by Django 3.2.7 on 2021-09-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_tokens', '0001_initial'),
        ('tokens', '0003_rename_status_token_active'),
        ('wallets', '0002_wallet_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='tokens',
            field=models.ManyToManyField(through='wallet_tokens.WalletTokens', to='tokens.Token'),
        ),
    ]
