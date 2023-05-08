from django.db import models

# Create your models here.
class cita(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    apellido = models.CharField(max_length=100, verbose_name='Apellido', null=True)
    identificacion = models.IntegerField(verbose_name='Identificacion', null=True)
    hora = models.TimeField(max_length=100, verbose_name='Hora', null=True)
    fecha = models.DateField(max_length = 10, verbose_name ='Fecha', null=True)
    medico = models.CharField(max_length= 100, verbose_name='Medico', null=True)


    def __str__(self):
        datos= "nombre: " + self.nombre + "apellido: "+ self.apellido + "identificacion: " + str(self.identificacion) + "hora: " + str(self.hora) + "fecha: " + str(self.fecha) + "medico: " + self.medico
        return datos