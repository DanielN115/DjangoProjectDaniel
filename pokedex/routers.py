from rest_framework import routers
from .views import *

# Routers
router=routers.DefaultRouter()
router.register(r'region', RegionViewSet)
router.register(r'pokemon', PokemonViewSet)
router.register(r'entrenador', EntrenadorViewSet)