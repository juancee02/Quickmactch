# Generated by Django 4.1 on 2022-09-06 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_rename_potencia_cartas_tiro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cartas',
            new_name='Cartas_A',
        ),
    ]
