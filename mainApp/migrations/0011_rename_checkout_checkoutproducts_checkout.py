# Generated by Django 4.1.2 on 2022-11-29 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_rename_ordrstatus_checkout_orderstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutproducts',
            old_name='Checkout',
            new_name='checkout',
        ),
    ]
