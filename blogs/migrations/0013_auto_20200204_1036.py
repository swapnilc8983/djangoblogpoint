# Generated by Django 3.0.2 on 2020-02-04 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_auto_20200204_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='blogs.Category'),
            preserve_default=False,
        ),
    ]