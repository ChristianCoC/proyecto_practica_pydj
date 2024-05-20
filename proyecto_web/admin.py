from django.contrib import admin
from . models import Persona, Libro  

# Register your models here.
class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1
    
class PersonaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'email', 'dni']
    list_display = ['nombre', 'email', 'dni']
    
    inlines = [LibroInline]
    
admin.site.register(Persona, PersonaAdmin)

class LibroAdmin(admin.ModelAdmin):
    fields = ['titulo', 'autor', 'persona_fk']
    list_display = ['titulo', 'autor', 'persona_fk']
    
admin.site.register(Libro, LibroAdmin)
