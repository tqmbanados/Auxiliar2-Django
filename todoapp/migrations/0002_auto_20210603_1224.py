# Generated by Django 3.1.1 on 2021-06-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateField(default='2021-06-03'),
        ),
    ]