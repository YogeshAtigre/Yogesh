# Generated by Django 5.0 on 2024-09-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0002_AddingEmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Country ID')),
                ('CountryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=' Department ID')),
                ('DeptName', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=30)),
            ],
        ),
    ]
