# Generated by Django 3.2.3 on 2021-06-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='achivements',
            field=models.ManyToManyField(blank=True, to='core.Achivement'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ManyToManyField(blank=True, to='core.Profile'),
        ),
    ]