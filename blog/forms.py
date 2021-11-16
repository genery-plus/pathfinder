from django import forms
from .models import Сharacter

class CharacterForm (forms.ModelForm):
    character_name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

    class Meta:
        model = Сharacter
        fields = '__all__'
