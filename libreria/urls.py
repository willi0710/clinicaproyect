from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('especialistas', views.especialistas, name='especialistas'),
    path('citas', views.citas, name='citas'),
    path('citas/solicitarGnral', views.solicitarGnral, name='solicitarGnral'),
    path('citas/modificar/<int:id>', views.modificar, name='modificar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    
]
