# Generated by Django 3.2 on 2022-11-03 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221103_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='short_descriptions',
            new_name='short_description',
        ),
    ]
