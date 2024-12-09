from django.urls import path

from app_coder import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    
    path('curso-formulario', views.formulario_curso_api, name="curso-formulario")
]