# Generated by Django 2.0 on 2019-01-12 16:27

from django.db import migrations, models
import showcase.file_size_validator


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_auto_20190110_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='scorecard_name',
            field=models.CharField(blank=True, help_text='Name matching scorecard field', max_length=100),
        ),
        migrations.AlterField(
            model_name='station',
            name='animation',
            field=models.FileField(blank=True, null=True, upload_to='stations', validators=[showcase.file_size_validator.file_size]),
        ),
        migrations.AlterField(
            model_name='station',
            name='diagram',
            field=models.FileField(blank=True, null=True, upload_to='stations', validators=[showcase.file_size_validator.file_size]),
        ),
        migrations.AlterField(
            model_name='station',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stations', validators=[showcase.file_size_validator.file_size]),
        ),
        migrations.AlterField(
            model_name='station',
            name='scorecard_diagram',
            field=models.FileField(blank=True, null=True, upload_to='stations', validators=[showcase.file_size_validator.file_size]),
        ),
        migrations.AlterField(
            model_name='station',
            name='webm_animation',
            field=models.FileField(blank=True, null=True, upload_to='stations', validators=[showcase.file_size_validator.file_size]),
        ),
    ]