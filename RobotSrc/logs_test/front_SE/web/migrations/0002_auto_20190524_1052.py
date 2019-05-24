# Generated by Django 2.2.1 on 2019-05-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='name',
        ),
        migrations.AddField(
            model_name='logs',
            name='time',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='logs',
            name='type',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='logs',
            name='info',
            field=models.CharField(default='', max_length=100),
        ),
    ]
