# Generated by Django 4.0.6 on 2022-07-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_created', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=10)),
            ],
        ),
    ]