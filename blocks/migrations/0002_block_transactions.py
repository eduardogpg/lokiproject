# Generated by Django 3.2.6 on 2021-08-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='transactions',
            field=models.IntegerField(default=0),
        ),
    ]
