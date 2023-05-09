# Generated by Django 4.2 on 2023-04-30 14:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del Plan de acciòn')),
                ('fecha_registro', models.DateField(default=datetime.datetime.now)),
                ('descripcionProblema', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion Problema ')),
                ('clasificacion', models.CharField(choices=[('critico', 'Critico'), ('mayor', 'Mayor'), ('critico', 'Critico'), ('menor', 'Menor'), ('critico', 'Critico'), ('informativo', 'Informativo')], max_length=300, verbose_name='Clasificacion')),
                ('normaIncumplida', models.CharField(max_length=300, verbose_name='Norma Incumplida')),
                ('tipoAccion', models.CharField(choices=[('mejora', 'MEJORA'), ('correctiva', 'CORRECTIVA')], max_length=300, verbose_name='Tipo Accion')),
                ('fuentePlan', models.CharField(choices=[('AUDITORÍA INTERNA', 'AUDITORÍA INTERNA'), ('AUDITORIA O VISITA EXTERNA', 'AUDITORIA O VISITA EXTERNA'), ('PAMEC ', 'PAMEC '), ('SEGUIMIENTO AL PROCESO', 'SEGUIMIENTO AL PROCESO'), ('ATENCIÓN A QUEJA,  RECLAMACIÓN O SUGERENCIA DEL  CLIENTE ', 'ATENCIÓN A QUEJA,  RECLAMACIÓN O SUGERENCIA DEL  CLIENTE '), ('SALIDAS NO CONFORMES ', 'SALIDAS NO CONFORMES '), ('REQUISITOS LEGALES /HABILITACIÓN  ', 'REQUISITOS LEGALES /HABILITACIÓN ')], max_length=300, verbose_name='Fuente Plan')),
                ('entidad', models.CharField(max_length=300, verbose_name='entidad')),
                ('proceso', models.CharField(choices=[('PLANEACIÓN ESTRATÉGICA', 'PLANEACIÓN ESTRATÉGICA'), ('GESTIÓN DE PROYECTOS', 'GESTIÓN DE PROYECTOS'), ('GESTIÓN DE LA INVESTIGACIÓN', 'GESTIÓN DE LA INVESTIGACIÓN '), ('SERVICIOS DE SALUD', 'SERVICIOS DE SALUD'), ('SERVICIOS AGRICOLAS ESPECIALIZADOS', 'SERVICIOS AGRICOLAS ESPECIALIZADOS'), ('FONDO EDITORIAL', 'FONDO EDITORIAL'), ('COMPRAS', 'COMPRAS'), ('GESTIÓN HUMANA', 'GESTIÓN HUMANA'), ('COMUNICACIONES Y MERCADEO', 'COMUNICACIONES Y MERCADEO'), ('INFRAESTRUCTURA Y SERVICIOS GENERALES ', 'INFRAESTRUCTURA Y SERVICIOS GENERALES '), ('GESTIÓN FINANCIERA', 'GESTIÓN FINANCIERA'), ('GESTIÓN DOCUMENTAL', 'GESTIÓN DOCUMENTAL')], max_length=300, verbose_name='proceso')),
                ('tratamientoInmediato', models.CharField(max_length=300, verbose_name='Tratamiento Inmediato')),
                ('evidencia', models.FileField(blank=True, null=True, upload_to='category/%Y/%m/%d', verbose_name='Evidencia')),
                ('fecha_correccion', models.DateField(default=datetime.datetime.now)),
                ('analisisCausa', models.CharField(max_length=300, verbose_name='Analisis Causa')),
                ('causaRaiz', models.CharField(max_length=300, verbose_name='Causa Raiz')),
                ('estado', models.CharField(max_length=300, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('responsable', models.CharField(blank=True, max_length=500, null=True, verbose_name='responsable')),
                ('img', models.FileField(blank=True, null=True, upload_to='evaluacion/%Y/%m/%d', verbose_name='img')),
                ('observaciones', models.CharField(max_length=300, unique=True, verbose_name='observaciones')),
                ('planMejora', models.CharField(max_length=300, unique=True, verbose_name='planMejora')),
                ('fecha_cierre', models.DateField(default=datetime.datetime.now)),
                ('estado', models.CharField(max_length=300, unique=True, verbose_name='estado')),
            ],
            options={
                'verbose_name': 'Evaluacion',
                'verbose_name_plural': 'Evaluaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('hallazgo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Hallazgo')),
                ('descripcionActividades', models.CharField(max_length=300, unique=True, verbose_name='Descripcion Actividades')),
                ('responsable', models.CharField(max_length=300, unique=True, verbose_name='responsable')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tarea/%Y/%m/%d', verbose_name='image')),
                ('fecha_inicio', models.DateField(default=datetime.datetime.now)),
                ('fecha_terminacion', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetPlanes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.category')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tarea')),
            ],
        ),
    ]
