# Generated by Django 3.2.7 on 2021-10-02 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0008_alter_token_abi'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='total_supply',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
