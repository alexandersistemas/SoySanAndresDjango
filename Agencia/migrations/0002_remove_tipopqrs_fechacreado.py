# Generated by Django 4.0.5 on 2022-07-01 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agencia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipopqrs',
            name='FechaCreado',
        ),
    ]
