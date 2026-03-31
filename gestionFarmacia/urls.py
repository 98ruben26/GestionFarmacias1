"""
URL configuration for gestionFarmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionFarmacia.views import present, accesoUsuario, registro_nuevo_view
from gestionFarmacia.views import login_credenciales_view, acceso_invitado_view 
#from gestionFarmacia.views import sucursales 
#from gestionFarmacia.views import productos 
from gestionFarmacia.views import lista_productos_general
from gestionFarmacia.views import inventario, ventas, lista_sucursales, detalle_sucursal
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('present/', present),
    path('accesoUsuario/', accesoUsuario),
    path('registroNuevo/', registro_nuevo_view),   
    path('loginCredenciales/', login_credenciales_view),
    path('accesoInvitado/', acceso_invitado_view),
    #path('sucursales/', sucursales),
    path('productos/', lista_productos_general, name='lista_productos'),
    #path('productos/', productos),
    path('inventario/', inventario),
    path('ventas/', ventas),
    path('sucursales/', lista_sucursales, name='lista_sucursales'),
    path('sucursal/<int:sucursal_id>/', detalle_sucursal, name='detalle_sucursal'),


    
]
# Al final de tus urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
