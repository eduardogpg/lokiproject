# Generated by Django 3.2.7 on 2021-10-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0013_remove_token_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='total',
            field=models.BigIntegerField(default=None),
            preserve_default=False,
        ),
    ]
