# Generated by Django 2.1.1 on 2018-10-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_picturemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturemessage',
            name='link',
            field=models.CharField(max_length=10000000),
        ),
    ]