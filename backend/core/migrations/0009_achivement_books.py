# Generated by Django 3.2.3 on 2022-05-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220508_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='achivement',
            name='books',
            field=models.ManyToManyField(to='core.Book'),
        ),
    ]