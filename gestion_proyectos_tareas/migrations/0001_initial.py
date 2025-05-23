# Generated by Django 5.1.7 on 2025-04-15 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('gestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='gestion_usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_limite', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Completada', 'Completada')], max_length=50)),
                ('prioridad', models.CharField(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=50)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='gestion_proyectos_tareas.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='TareaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_proyectos_tareas.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario')),
            ],
            options={
                'unique_together': {('tarea', 'usuario')},
            },
        ),
        migrations.AddField(
            model_name='tarea',
            name='asignados',
            field=models.ManyToManyField(related_name='tareas_asignadas', through='gestion_proyectos_tareas.TareaUsuario', to='gestion_usuarios.usuario'),
        ),
    ]
