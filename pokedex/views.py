from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, World")


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
    