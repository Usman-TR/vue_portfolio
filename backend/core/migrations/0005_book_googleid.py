# Generated by Django 3.2.3 on 2022-05-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_markrequest_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='GoogleId',
            field=models.CharField(default='', max_length=150),
        ),
    ]
