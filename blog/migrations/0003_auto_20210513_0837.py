# Generated by Django 3.2.2 on 2021-05-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210513_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='cmd_strength_modifier',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='floor',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
