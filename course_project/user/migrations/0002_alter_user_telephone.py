# Generated by Django 4.0.6 on 2022-08-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.BigIntegerField(max_length=12, unique=True),
        ),
    ]
