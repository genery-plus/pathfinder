# Generated by Django 3.2.2 on 2021-05-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='cmd_strength_modifier',
        ),
        migrations.RemoveField(
            model_name='character',
            name='floor',
        ),
    ]
