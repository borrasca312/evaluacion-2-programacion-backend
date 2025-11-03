from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('nueva', 'Nueva'),
        ('en_progreso', 'En progreso'),
        ('cerrada', 'Cerrada'),
    ]
    PRIORIDAD_CHOICES = [
        ('low', 'Baja'),
        ('med', 'Media'),
        ('high', 'Alta'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nueva')
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='med')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"

class Comentario(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cuerpo = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.solicitud}"
