# Generated by Django 2.0.8 on 2018-10-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Unregistered', 'Unregistered'), ('Player', 'Player'), ('Coach', 'Coach'), ('Director', 'Director'), ('Agent', 'Agent'), ('Referee', 'Referee')], default='Unregistered', help_text='First Name', max_length=100),
        ),
    ]
