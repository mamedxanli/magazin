# Generated by Django 2.0.6 on 2018-12-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Остаток в кассе'),
        ),
    ]
