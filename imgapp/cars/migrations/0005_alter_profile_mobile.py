# Generated by Django 3.2.9 on 2021-11-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20211121_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
