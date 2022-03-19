# Generated by Django 4.0.1 on 2022-02-26 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('image_ingredient', models.ImageField(default=None, null=True, upload_to='ingredient_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=1)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributors.distributors')),
            ],
        ),
    ]
