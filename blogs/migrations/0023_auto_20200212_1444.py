# Generated by Django 3.0.2 on 2020-02-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0022_auto_20200210_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
