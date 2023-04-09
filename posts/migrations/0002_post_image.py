# Generated by Django 4.1.7 on 2023-04-08 11:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]