# Generated by Django 3.2 on 2022-12-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]