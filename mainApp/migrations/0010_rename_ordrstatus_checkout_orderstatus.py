# Generated by Django 4.1.2 on 2022-11-29 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_alter_checkoutproducts_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='ordrstatus',
            new_name='orderstatus',
        ),
    ]
