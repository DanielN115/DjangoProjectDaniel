from django.contrib import admin
from django.urls import path, include
from pokedex import views
from pokedex import routers
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', views.home_page_view, name='HomePage'),
    path('api/', include(routers.router.urls), name='ApiRestFramework'),
    path('api/docs/', include_docs_urls(title='Api Documentation'), name='ApiRestFrameworkDocument'),
    path('pokeapi/', views.pokeapi_view, name='PokeApi'),
]