import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, World")

def pokeapi_view(request):
    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'].lower() #busqueda minusculas
            pokemon = pokemon.replace(' ', '%20') # elimina espacion

            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}') # urls api
            url_pokeapi.add_header('User-Agent', "pikachu") # header
            
            source = urllib.request.urlopen(url_pokeapi).read() # trae el archivo
            list_of_data = json.loads(source) # transorma en diccionario
            
            # Altura de decímetros a metros
            height_obtained = (float(list_of_data['height']) * 0.1)
            height_rounded = round(height_obtained, 2)

            # Peso de hectogramos a kilogramos
            weight_obtained = (float(list_of_data['weight']) * 0.1)
            weight_rounded = round(weight_obtained, 2)

            data = {
                "number": str(list_of_data['id']),
                "name": str(list_of_data['name']).capitalize(),
                "height": str(height_rounded)+ " m",
                "weight": str(weight_rounded)+ " kg",
                "sprite": str(list_of_data['sprites']['front_default']),
            }
            print(data)
        else:
            data = {}
        
        return render(request, 'pokeapi.html', data)
    except HTTPError as e:
            if e.code == 404:
                return render(request, "404.html")
    


# Views RestFramework
class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    
class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    
class EntrenadorViewSet(viewsets.ModelViewSet):
    serializer_class = EntrenadorSerializer
    queryset = Entrenador.objects.all()
    
