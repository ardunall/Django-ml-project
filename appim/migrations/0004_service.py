# Generated by Django 5.0.3 on 2024-04-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appim', '0003_rename_image_doctor_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon_class', models.CharField(max_length=50)),
            ],
        ),
    ]
