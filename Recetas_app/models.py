from django.db import models
from django.utils.timezone import now # Importa la función now()para manejar fechas y horas en el modelo.




#Insumos temporales hasta tener los reales
class InsumoTemporal(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


    
class IngredienteReceta(models.Model):
    insumo = models.ForeignKey(InsumoTemporal, on_delete=models.PROTECT) #CHECHAR LO DE PROTECT
    cantidad_necesaria = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cantidad de insumo necesaria para la receta")

   

class Recetas(models.Model):
    NombreReceta = models.TextField(max_length=100)
    cantidad_galletas = models.DecimalField(max_digits=10, decimal_places=2)
    ingredientes = models.ForeignKey(IngredienteReceta, on_delete=models.CASCADE,blank=True,null=True)#RELACION UNO A MUCHOS "FOREINGKEY"
    class Meta:#PARA CONFIGURACIONES EXTRA AL MODELO
        permissions = [("...", "...")]#PERMISOS POR DEFINIR
        #ordering = ['-fecha_creacion']
    def __str__(self):
        return f"{self.id} - {self.NombreReceta}"
    