# Generated by Django 3.2 on 2021-08-21 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0003_auto_20210821_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_image',
            new_name='image',
        ),
    ]