from django import forms
from .models import onlineDictionary

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = onlineDictionary
        fields = ['letter','word','defination','exmaple']
