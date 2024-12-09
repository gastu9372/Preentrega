from django.shortcuts import render, redirect

from .models import Curso, Profesor
from .forms import CursoFormulario

# Create your views here.
def inicio(request):
    return render(request, "app_coder/index.html")

def cursos(request):
    
    query = request.GET.get("q")
    if query:
        cursos = Curso.objects.filter(nombre__icontains=query) | Curso.objects.filter(comision__icontains=query)
    else:
        cursos = Curso.objects.all()
    return render(request, "app_coder/cursos.html", {"cursos":cursos})

def profesores(request):
    
    query = request.GET.get("q")
    if query:
        profes = Profesor.objects.filter(nombre__icontains=query)
    else:
        profes = Profesor.objects.all()
    return render(request, "app_coder/profesores.html", {"profes":profes})
    

def estudiantes(request):
    return render(request, "app_coder/estudiantes.html")

def entregables(request):
    return render(request, "app_coder/entregables.html")


def formulario_curso(request):
    
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"],comision=request.POST["comision"])
        curso.save()
        return redirect("cursos")
    else:
        return render(request, "app_coder/forms/curso-formulario.html")


def formulario_curso_api(request):
    
    if request.method == "POST":
        curso_form = CursoFormulario(request.POST)

        if curso_form.is_valid():
            info_limpia = curso_form.cleaned_data
            curso = Curso(nombre=info_limpia["nombre"],comision=info_limpia["comision"])
            curso.save()
            return redirect("cursos")
    else:
        curso_form = CursoFormulario()

    contexto = {"form": curso_form}

    return render(request, "app_coder/forms/curso-formulario.html", contexto)



