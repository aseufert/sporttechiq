# Generated by Django 2.0 on 2019-01-12 16:37

from django.db import migrations, models
import showcase.file_size_validator


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0007_auto_20190112_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldlayout',
            name='diagram',
            field=models.FileField(blank=True, null=True, upload_to='field-layouts', validators=[showcase.file_size_validator.file_size]),
        ),
        migrations.AlterField(
            model_name='fieldlayout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='field-layouts', validators=[showcase.file_size_validator.file_size]),
        ),
    ]