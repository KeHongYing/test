# Generated by Django 2.1.1 on 2018-10-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talker', models.CharField(max_length=20)),
                ('message', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
