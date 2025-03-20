from django.urls import path
from .views import lista_estudiantes, agregar_estudiante, editar_estudiante, eliminar_estudiante

urlpatterns = [
    path('', lista_estudiantes, name='lista_estudiantes'),
    path('agregar/', agregar_estudiante, name='agregar_estudiante'),
    path('editar/<int:id>/', editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:id>/', eliminar_estudiante, name='eliminar_estudiante'),
]