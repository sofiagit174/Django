# filepath: c:\Users\Danna\Downloads\CREAR\estudiantes\estudiantes_app\views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiante.html', {'estudiantes': estudiantes})

def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        correo = request.POST['correo']
        Estudiante.objects.create(nombre=nombre, edad=edad, correo=correo)
        return redirect('lista_estudiantes')
    return render(request, 'agregar_estudiante.html')

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.nombre = request.POST['nombre']
        estudiante.edad = request.POST['edad']
        estudiante.correo = request.POST['correo']
        estudiante.save()
        return redirect('lista_estudiantes')
    return render(request, 'editar_estudiante.html', {'estudiante': estudiante})

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('lista_estudiantes')