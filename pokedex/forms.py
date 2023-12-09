from django import forms
from .models import Region,Pokemon,Entrenador

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        
class PokemonForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        
class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'