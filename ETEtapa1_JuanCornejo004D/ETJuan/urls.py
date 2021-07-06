from django.urls import path
from .views import home, crear_colab, inicio, modificar_colab, modificar, eliminar

urlpatterns = [
    path('home', home,name="home"),
    path('crear_colab', crear_colab, name="crear_colab"),
    path('', inicio, name='inicio'),
    path('modificar_colab', modificar_colab, name="modificar_colab"),
    path('modificar/<id>',modificar, name="modificar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
]   