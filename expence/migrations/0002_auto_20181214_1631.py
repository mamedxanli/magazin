# Generated by Django 2.0.6 on 2018-12-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expence',
            name='purpose',
            field=models.CharField(default=None, max_length=100, verbose_name='Назначение'),
        ),
    ]
