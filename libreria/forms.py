from django import forms
from .models import cita

class citaForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = '__all__'
