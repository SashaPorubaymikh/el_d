# Generated by Django 2.2.5 on 2019-09-28 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20190921_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
