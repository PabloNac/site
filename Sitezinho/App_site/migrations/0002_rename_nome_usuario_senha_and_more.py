# Generated by Django 5.0.6 on 2024-06-27 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Nome',
            new_name='Senha',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Sobre_Nome',
            new_name='Usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Idade',
        ),
    ]
