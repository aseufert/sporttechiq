# Generated by Django 2.0 on 2019-02-04 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190203_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='header',
        ),
    ]
