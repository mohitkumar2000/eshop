# Generated by Django 4.1.2 on 2022-11-21 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='name',
            new_name='product',
        ),
    ]
