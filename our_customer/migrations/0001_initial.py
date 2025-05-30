# Generated by Django 5.2 on 2025-05-03 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('intro_title', models.CharField(max_length=255)),
                ('intro_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='customers/logos/')),
                ('description', models.TextField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='our_customer.customermainpage')),
            ],
        ),
    ]
