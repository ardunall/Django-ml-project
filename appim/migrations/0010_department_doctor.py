# Generated by Django 5.0.3 on 2024-05-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appim', '0009_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='Doctor',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]