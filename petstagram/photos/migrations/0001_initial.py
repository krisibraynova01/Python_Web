# Generated by Django 5.0.2 on 2024-02-16 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pet_photos/')),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_publication', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, to='pets.pet')),
            ],
        ),
    ]