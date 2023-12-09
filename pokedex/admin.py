from django.contrib import admin
from .models import Region,Pokemon,Entrenador
from .forms import RegionForm,PokemonForm,EntrenadorForm
# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    form = RegionForm
    
class PokemonAdmin(admin.ModelAdmin):
    form = PokemonForm
    
class EntrenadorAdmin(admin.ModelAdmin):
    form = EntrenadorForm

admin.site.register(Region, RegionAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Entrenador, EntrenadorAdmin)