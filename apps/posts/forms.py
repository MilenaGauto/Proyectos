from django import forms
from .models import Comentrario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentrario
        fields = ['texto']
