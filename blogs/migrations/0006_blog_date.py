# Generated by Django 3.0.2 on 2020-02-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Date',
            field=models.DateField(default='2016-12-12'),
            preserve_default=False,
        ),
    ]
