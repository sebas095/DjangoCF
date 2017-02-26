from django.shortcuts import render
from django.http import HttpResponse

def index_adopcion(request):
    return HttpResponse('Soy la pagina principal de la app adopcion')

