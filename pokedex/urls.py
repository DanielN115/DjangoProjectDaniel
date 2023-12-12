from django.contrib import admin
from django.urls import path, include
from pokedex import views
from pokedex import routers
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', views.home_page_view, name='HomePage'),
    path('region/', views.regiones_list_view, name='Region_List'),
    path('region/<int:id>/', views.regiones_detail_view, name='Region_Detail'),
    path('entrenador/', views.entrenador_list_view, name='Entrenador_List'),
    path('entrenador/<int:id>/', views.entrenador_detail_view, name='Entrenador_Detail'),
    path('pokemon/', views.pokemon_list_view, name='Pokemon_List'),
    path('pokemon/<int:id>/', views.pokemon_detail_view, name='Pokemon_Detail'),
    path('api/', include(routers.router.urls), name='ApiRestFramework'),
    path('api/docs/', include_docs_urls(title='Api Documentation'), name='ApiRestFrameworkDocument'),
    path('pokeapi/', views.pokeapi_view, name='PokeApi'),
]