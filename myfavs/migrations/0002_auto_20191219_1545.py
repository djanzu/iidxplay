# Generated by Django 3.0.1 on 2019-12-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfavs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='h',
            field=models.IntegerField(default=None, verbose_name='Hyper'),
        ),
        migrations.AlterField(
            model_name='music',
            name='a',
            field=models.IntegerField(default=None, verbose_name='Another'),
        ),
        migrations.AlterField(
            model_name='music',
            name='n',
            field=models.IntegerField(default=None, verbose_name='Normal'),
        ),
    ]