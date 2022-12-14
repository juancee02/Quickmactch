# Generated by Django 4.1 on 2022-09-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0005_rename_cartas_cartas_a'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas_B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posocion', models.CharField(max_length=100)),
                ('fuerza', models.CharField(max_length=100)),
                ('tiro', models.CharField(max_length=100)),
                ('velocidad', models.CharField(max_length=100)),
                ('rendimiento_total', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cartas_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posocion', models.CharField(max_length=100)),
                ('fuerza', models.CharField(max_length=100)),
                ('tiro', models.CharField(max_length=100)),
                ('velocidad', models.CharField(max_length=100)),
                ('rendimiento_total', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cartas_D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posocion', models.CharField(max_length=100)),
                ('fuerza', models.CharField(max_length=100)),
                ('tiro', models.CharField(max_length=100)),
                ('velocidad', models.CharField(max_length=100)),
                ('rendimiento_total', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
