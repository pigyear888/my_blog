# Generated by Django 3.2 on 2021-06-07 08:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_articlepost_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]