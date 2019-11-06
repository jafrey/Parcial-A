from django.db import models

# Create your models here.

class cancion(models.Model):
    nom_cancion = models.CharField(max_length=30)
    desc_cancion = models.CharField(max_length=30)
    anio_salida = models.IntegerField()

    class Meta:
        verbose_name = "Cancion"
        verbose_name_plural = "Canciones"

    def __str__(self):
        return self.nom_cancion
