# Generated by Django 4.1.3 on 2022-12-15 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_product_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
