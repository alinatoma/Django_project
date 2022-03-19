# Generated by Django 4.0.1 on 2022-02-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]