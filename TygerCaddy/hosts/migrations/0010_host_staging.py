# Generated by Django 2.0.3 on 2018-05-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('hosts', '0009_auto_20180513_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='staging',
            field=models.BooleanField(default=False),
        ),
    ]