# Generated by Django 5.1.6 on 2025-02-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphankid',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='orphan_images/'),
        ),
    ]
