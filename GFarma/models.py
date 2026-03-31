from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    password = models.CharField(max_length=128) # En producción usa los modelos de Auth de Django
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo# Create your models here.

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    imagen = models.ImageField(upload_to='sucursales/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Sucursales"

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # El argumento correcto es 'through'
    sucursales = models.ManyToManyField(
        'Sucursal', 
        through='Inventario', 
        related_name='productos'
    )

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    """
    Modelo intermedio para gestionar el stock específico de cada producto
    en cada sucursal.
    """
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    pasillo_ubicacion = models.CharField(max_length=50, blank=True)

    class Meta:
        # Evita que se duplique la entrada de un mismo producto en una misma sucursal
        unique_together = ('sucursal', 'producto')

    def __str__(self):
        return f"{self.producto.nombre} en {self.sucursal.nombre} ({self.stock} unid.)"

class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.producto.nombre} ({self.fecha_pedido.date()})"