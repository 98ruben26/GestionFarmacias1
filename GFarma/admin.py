from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count, Sum
from .models import Sucursal, Producto, Inventario, Pedido

# 1. Configuración para ver Usuarios Registrados
# Extendemos el UserAdmin original para ver la fecha de registro
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff')
    list_filter = ('date_joined', 'is_staff')
    ordering = ('-date_joined',) # Los más recientes primero

admin.site.unregister(User) # Quitamos el registro por defecto
admin.site.register(User, CustomUserAdmin) # Registramos nuestra versión mejorada

# 2. Configuración para analizar Tendencias de Productos
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'usuario', 'cantidad', 'fecha_pedido', 'get_temporada')
    list_filter = ('fecha_pedido', 'producto')
    date_hierarchy = 'fecha_pedido' # Agrega una barra de navegación por fechas (años, meses, días)

    def get_temporada(self, obj):
        """Calcula la temporada basada en el mes del pedido"""
        mes = obj.fecha_pedido.month
        if mes in [12, 1, 2]: return "Verano ☀️"
        elif mes in [3, 4, 5]: return "Otoño 🍂"
        elif mes in [6, 7, 8]: return "Invierno ❄️"
        else: return "Primavera 🌸"
    get_temporada.short_description = 'Temporada'

# 3. Reporte de "Lo más pedido" en la lista de Productos
#@admin.register(Producto)
#class ProductoAdmin(admin.ModelAdmin):
#    list_display = ('nombre', 'precio', 'total_vendido')
    
#    def get_queryset(self, request):
        # Anotamos cada producto con la suma total de sus pedidos
#        queryset = super().get_queryset(request)
#        queryset = queryset.annotate(_total_vendido=Sum('pedido__cantidad'))
#        return queryset

#    def total_vendido(self, obj):
#        return obj._total_vendido or 0
#    total_vendido.admin_order_field = '_total_vendido'
#    total_vendido.short_description = 'Unidades Vendidas'

# Permite editar el stock directamente dentro de la página de Producto o Sucursal
class InventarioInline(admin.TabularInline):
    model = Inventario
    extra = 1 # Muestra un espacio vacío para agregar un nuevo registro rápidamente

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion')
    inlines = [InventarioInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)
    list_filter = ('sucursales',)
    inlines = [InventarioInline]

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'sucursal', 'stock', 'pasillo_ubicacion')
    list_filter = ('sucursal', 'producto')
    search_fields = ('producto__nombre', 'sucursal__nombre')
    list_editable = ('stock', 'pasillo_ubicacion') # Permite editar el stock desde la lista principal

# Register your models here.
