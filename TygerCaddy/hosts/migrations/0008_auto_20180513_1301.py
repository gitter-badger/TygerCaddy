# Generated by Django 2.0.3 on 2018-05-13 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0007_config_dns_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='dns_provider',
        ),
        migrations.DeleteModel(
            name='Config',
        ),
    ]