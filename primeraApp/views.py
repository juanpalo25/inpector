from django.http import HttpResponse
from datetime import datetime
from django.template import Context, loader
from django.template import Template

def inicio(request):
    return HttpResponse('Hola primera vista.')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Estamos a: {fecha_actual}')

def mi_template(request):
    template1 = loader.get_template('prueba.html')
    nombre= 'Inspector'
    lista = [1, 2, 3, 4, 5, 6, 7]
    render1 = template1.render({'nombre': nombre, 'edad': 4600, 'lista': lista})
    return HttpResponse(render1) 