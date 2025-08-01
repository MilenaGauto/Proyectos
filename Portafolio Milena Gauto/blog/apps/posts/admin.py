# Register your models here.
from django.contrib import admin
from .models import Categoria, Post, Comentrario

# Register your models here. 

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')




admin.site.register(Categoria)

admin.site.register(Comentrario)