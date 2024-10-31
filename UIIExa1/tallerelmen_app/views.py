from django.shortcuts import render
from .models import Productos
# Create your views here.

def inicio_vista(request):
    # Obtener todos los registros de la tabla Materia
    Listadoproductos = Productos.objects.all()
    return render (request, 'gestionarProductos.html',{"Losproductos":Listadoproductos})