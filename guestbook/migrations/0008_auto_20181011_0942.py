# Generated by Django 2.1.1 on 2018-10-11 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0007_auto_20181011_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturemessage',
            name='link',
            field=models.CharField(max_length=100000),
        ),
    ]
