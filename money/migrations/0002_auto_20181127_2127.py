# Generated by Django 2.0.6 on 2018-11-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
