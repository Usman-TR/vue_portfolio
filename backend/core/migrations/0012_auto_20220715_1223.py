# Generated by Django 3.2.3 on 2022-07-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_recomendationbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='no language', max_length=14),
        ),
        migrations.AddField(
            model_name='book',
            name='publishedDate',
            field=models.CharField(default='no date', max_length=15),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='no publisher', max_length=70),
        ),
    ]