# Generated by Django 5.0.6 on 2024-07-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_rename_descripcionproyecto_proyectos_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='descripcion',
            field=models.TextField(max_length=300),
        ),
    ]
