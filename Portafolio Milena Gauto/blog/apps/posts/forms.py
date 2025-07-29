from django import forms
from .models import Comentrario, Post, Categoria


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentrario
        fields = ['texto']

class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
