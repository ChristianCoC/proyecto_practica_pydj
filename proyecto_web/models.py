from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email", null=False, blank=False)
    dni = models.IntegerField(verbose_name="DNI", null=False, blank=False, default=0)

    class Meta:
        db_table = "persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        
    def __str__(self) -> str:
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    autor = models.CharField(max_length=255, verbose_name="Autor")
    persona_fk = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        


