# Generated by Django 2.2 on 2021-05-15 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_auto_20210515_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'permissions': (('update_home', 'Update Home'),)},
        ),
    ]
