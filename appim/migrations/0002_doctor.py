# Generated by Django 5.0.3 on 2024-04-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
