# Generated by Django 3.0.2 on 2020-02-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0029_auto_20200213_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/docslogo.png', null=True, upload_to='images/'),
        ),
    ]
