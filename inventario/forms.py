from django import forms
from .models import Solicitud, Comentario

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ["titulo", "descripcion", "categoria", "prioridad"]

    def clean_titulo(self):
        titulo = self.cleaned_data.get("titulo", "").strip()
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return titulo

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion", "").strip()
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["cuerpo"]

    def clean_cuerpo(self):
        cuerpo = self.cleaned_data.get("cuerpo", "").strip()
        if not cuerpo:
            raise forms.ValidationError("El comentario no puede estar vacío.")
        return cuerpo
