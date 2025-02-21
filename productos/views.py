import json
from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse
from .forms import productoForms


# Create your views here.
def lista_productos(request):
    #Obtener todos los objetos de productos de la base de datos
    productos = Producto.objects.all();
    #Guardar los datos en un diccionario
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
            
    ]
    
    return JsonResponse(data, safe = False)

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ver.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = productoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = productoForms()
    return render(request, 'agregar.html', {'form': form})


# Vista que devuelve los Productos como JSON
def lista_productos(request):
    ...

def ver_productos(request):
    return render(request, 'ver.html')

# Función que agrega un producto con un objeto JSON
def registrar_producto(request):
    # Checar si nuestra request es de tipo POST
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parámetro es un texto que debería ser un JSON
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            )
            # create directamente mete el objeto en la BD
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': producto.id
                }, 
                status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse({'error': str(e)}, status=400)

    # Si no es POST el request...
    return JsonResponse(
        {'error': 'El método no está soportado'}, status=405
        )


from django.shortcuts import get_object_or_404
#funciones para el metodo put
def actualizar_producto(request, id_producto):
    if request.method=='PUT':
        producto= get_object_or_404(Producto, id=id_producto)
        try:
            #La informacion de la modificacion del producto viene del body del rewquest 
            data = json.loads(request.body)
            producto.nombre=data.get('nombre', producto.nombre)
            producto.precio=data.get('precio', producto.precio)
            producto.imagen=data.get('imagen', producto.imagen)
            producto.save()
            return JsonResponse({'mensaje': 'Producto actuaalizado correctamente '}, status=200)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=400)
    return JsonResponse ({'error':'Metodo no es PUT'}, status=405)


#funcion para delete 
def borrar_producto(request, id_producto):
    if request.method=='DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete()#Borra fisiscamente el registro de la base de datos 
        return JsonResponse({'mensaje':'Producto eliminado correctamente'}, status=200)
    return JsonResponse ({'error':'El metodo no es delete'}, status=405)

#función pra un get especifico
def obtener_productos (request, id_producto):
    if request.method=='GET':
        producto = get_object_or_404(Producto, id=id_producto)
        data={
            "id": producto.id,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "imagen": producto.imagen
        }
        return JsonResponse(data, status=200)
    return JsonResponse ({'error':'El metodo no es delete'}, status=405)
