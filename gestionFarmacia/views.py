from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render , redirect, get_object_or_404
from GFarma.models import Usuario, Sucursal, Producto
from django.contrib.auth import authenticate, login


def present(request):
    return render(request, "plantillaPresentacion.html")
    #return HttpResponse("¡Bienvenido a la gestión de farmacias!")
def accesoUsuario(request):
    return render(request, "accesoUsuario.html")
def registro_nuevo_view(request):
    if request.method == 'POST':
        # Captura de datos del formulario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        
        # Guardado en la base de datos
        nuevo_usuario = Usuario(nombre_completo=nombre, correo_electronico=email, password=passw)
        nuevo_usuario.save()
        
        return redirect('/accesoUsuario/') # Redirige tras el éxito
        
    return render(request, "registroNuevo.html")

def login_credenciales_view(request):
    if request.method == 'POST':
        # 1. Obtener los datos del formulario (coincidiendo con los 'name' del HTML)
        usuario = request.POST.get('username')
        clave = request.POST.get('password')

        # 2. Validar contra la base de datos
        # authenticate busca al usuario y verifica que la contraseña coincida
        user = authenticate(request, username=usuario, password=clave)

        if user is not None:
            # 3. Si las credenciales son correctas, se crea la sesión
            login(request, user)
            # Redirigir a la página de productos tras éxito
            return redirect('/sucursales/') 
        else:
            # 4. Si fallan, puedes enviar un mensaje de error a la plantilla
            return render(request, "loginCredenciales.html", {
                "error": "Usuario o contraseña incorrectos"
            })

    return render(request, "loginCredenciales.html")

def acceso_invitado_view(request):
    return render(request, "accesoInvitado.html")

#def sucursales(request):
    #return HttpResponse("Aquí se mostrarán las sucursales disponibles.")
    #return render(request, "sucursales.html")

def lista_sucursales(request):
    # Obtenemos las primeras 5 sucursales
    sucursales = Sucursal.objects.all()[:5] 
    return render(request, 'sucursales.html', {'sucursales': sucursales})

def detalle_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursal, id=sucursal_id)
    # Suponiendo que tienes una relación ManyToMany o ForeignKey en tu modelo Producto
    productos = Producto.objects.filter(sucursales=sucursal)
    
    return render(request, 'detalleSucursal.html', {
        'sucursal': sucursal,
        'productos': productos
    })


def lista_productos_general(request):
    # Obtenemos todos los productos registrados en el sistema
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos': productos}) 

def productos(request):
    return HttpResponse("Aquí se mostrarán los productos disponibles.")
def inventario(request):
    return HttpResponse("Aquí se mostrará el inventario de cada sucursal.")
def ventas(request):
    return HttpResponse("Aquí se mostrarán las ventas realizadas.")

    