from django import forms
from .models import character

class CharacterForm (forms.ModelForm):
    class Meta:
        model = character
        fields = '__all__'