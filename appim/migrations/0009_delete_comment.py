# Generated by Django 5.0.3 on 2024-05-29 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appim', '0008_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]