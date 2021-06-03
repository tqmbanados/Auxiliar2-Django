from django.shortcuts import render, redirect

# Create your views here.
from todoapp.models import Tarea
from categorias.models import Categoria


def tareas(request):  # the index view
    mis_tareas = Tarea.objects.all()  # quering all todos with the object manager
    categorias = Categoria.objects.all()  # getting all categories with object manager

    if request.method == "GET":
        return render(request, "todoapp/index.html",
                      {"tareas": mis_tareas, "categorias": categorias})
