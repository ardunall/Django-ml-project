# Generated by Django 5.0.3 on 2024-05-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
