# Generated by Django 2.1.1 on 2018-10-11 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0004_auto_20181005_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturemessage',
            name='link',
            field=models.CharField(max_length=10000),
        ),
    ]
