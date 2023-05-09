from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import clasificacion_choices,fuentePlan_choices, tipoAccion_choices, proceso_choices
from core.models import BaseModel
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del Plan de acciòn')
    fecha_registro= models.DateField(default=datetime.now)
    descripcionProblema  = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion Problema ')
    clasificacion = models.CharField(max_length=300, choices=clasificacion_choices, verbose_name='Clasificacion')
    normaIncumplida = models.CharField(max_length=300, verbose_name='Norma Incumplida')
    tipoAccion = models.CharField(max_length=300,  choices=tipoAccion_choices,  verbose_name='Tipo Accion')
    fuentePlan = models.CharField(max_length=300, choices=fuentePlan_choices,  verbose_name='Fuente Plan')
    entidad = models.CharField(max_length=300, verbose_name='entidad')
    proceso = models.CharField(max_length=300, choices=proceso_choices,  verbose_name='proceso')
    tratamientoInmediato = models.CharField(max_length=300, verbose_name='Tratamiento Inmediato')
    evidencia = models.FileField(upload_to='category/%Y/%m/%d', null=True, blank=True, verbose_name='Evidencia')
    fecha_correccion= models.DateField(default=datetime.now)
    analisisCausa= models.CharField(max_length=300, verbose_name='Analisis Causa')
    causaRaiz = models.CharField(max_length=300, verbose_name='Causa Raiz')
    estado = models.CharField(max_length=300, verbose_name='Estado')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['evidencia'] = self.get_evidencia()
        item['fecha_registro'] = self.fecha_registro.strftime('%Y-%m-%d')
        return item
    


    def get_evidencia(self):
        if self.evidencia:
            return '{}{}'.format(MEDIA_URL, self.evidencia)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']




#Tareea


class Tarea(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    
    hallazgo = models.CharField(max_length=500, null=True, blank=True, verbose_name='Hallazgo')
    descripcionActividades = models.CharField(max_length=300, verbose_name='Descripcion Actividades', unique=True)
    responsable= models.CharField(max_length=300, verbose_name='responsable', unique=True)
    image = models.ImageField(upload_to='tarea/%Y/%m/%d', null=True, blank=True, verbose_name='image')
    fecha_inicio= models.DateField(default=datetime.now)
    fecha_terminacion= models.DateField(default=datetime.now)
    

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        item['fecha_inicio'] = self.fecha_inicio.strftime('%Y-%m-%d')
        return item
    


    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['id']



class DetPlanes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.tarea.name
#
class Evaluacion(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    date_joined = models.DateField(default=datetime.now)
    responsable  = models.CharField(max_length=500, null=True, blank=True, verbose_name='responsable')
    img = models.FileField(upload_to='evaluacion/%Y/%m/%d', null=True, blank=True, verbose_name='img')
    observaciones = models.CharField(max_length=300, verbose_name='observaciones', unique=True)
    planMejora = models.CharField(max_length=300, verbose_name='planMejora', unique=True)
    fecha_cierre= models.DateField(default=datetime.now)
    estado = models.CharField(max_length=300, verbose_name='estado', unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['img'] = self.get_img()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        
        return item
    


    def get_img(self):
        if self.img:
            return '{}{}'.format(MEDIA_URL, self.img)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['id']

