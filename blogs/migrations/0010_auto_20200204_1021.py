# Generated by Django 3.0.2 on 2020-02-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20200204_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
