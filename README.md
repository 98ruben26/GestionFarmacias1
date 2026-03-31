#diplomado de FULLSTACK
Desarrollado por Ruben Ariel Acosta Aguilar

# FarmaGest Pro 💊

**FarmaGest Pro** es un sistema de gestión farmacéutica integral desarrollado con **Django** y **PostgreSQL**. El proyecto permite la administración centralizada de múltiples sucursales, control de inventario dinámico y un catálogo de productos accesible para los usuarios según su ubicación geográfica.

## 🚀 Características Principales

- **Gestión Multi-Sucursal:** Visualización dinámica de sedes con redirección a inventarios específicos.
- **Inventario Inteligente:** Relación Muchos-a-Muchos entre productos y sucursales mediante una tabla intermedia (`through='Inventario'`) que gestiona stock y ubicación física (pasillos).
- **Panel Administrativo Avanzado:** Inlines configurados para editar stock directamente desde la ficha de sucursal o producto.
- **Análisis de Tendencias:** Seguimiento de pedidos y usuarios con reportes automáticos por temporadas del año.
- **Arquitectura Escalable:** Diseño basado en el patrón MVT de Django y persistencia de datos en PostgreSQL.

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.x, Django Framework.
- **Base de Datos:** sqlite3.
- **Frontend:** HTML5, CSS3 (Custom Styles), Bootstrap 5.
- **Control de Versiones:** Git & GitHub.

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- Python (v3.8+)
- PostgreSQL
- Virtualenv

## 🔧 Instalación y Configuración

1. **Clonar el repositorio:**
   """bash
   git clone [https://github.com/tu-usuario/FarmaGest-Pro.git]
   cd FarmaGest-Pro
Crear y activar entorno virtual:
   """bash

    python -m venv venv
    # En Windows:
    venv\Scripts\activate

    Instalar dependencias:
    """bash

    pip install django psycopg2-binary pillow

    Configurar la base de datos:
    Asegúrate de tener creada una base de datos en PostgreSQL y configurar las credenciales en el archivo settings.py.

    Aplicar migraciones:
    Bash

    python manage.py makemigrations
    python manage.py migrate

    Crear superusuario (Admin):
    Bash

    python manage.py createsuperuser

    Iniciar el servidor:
    Bash

    python manage.py runserver

📸 Previsualización de Sucursales

La sección de infraestructura permite a los usuarios seleccionar la sede más cercana:

    Nota: El sistema utiliza validaciones de seguridad para asegurar que cada sucursal muestre únicamente el stock disponible en su base de datos local.

🔒 Seguridad e Infraestructura

Como parte del enfoque en ciberseguridad industrial, este proyecto implementa:

    Validación de existencia de medios (imágenes) para evitar fugas de rutas o errores de servidor.

    Control de acceso granular mediante decoradores de Django.

    Estructura de modelos diseñada para prevenir colisiones de datos en entornos distribuidos.

Desarrollado por [Tu Nombre] - Postgraduate Student in Technical Fields & Infrastructure Lead.


---

### Recomendaciones adicionales:

1.  **Imágenes:** Si tienes capturas de pantalla de la página de sucursales o del admin, crea una carpeta llamada `screenshots/` en tu repo y añádelas al README para que sea más visual.
2.  **Licencia:** Considera añadir un archivo `LICENSE` (como MIT) si planeas que el código sea abierto.
3.  **Wiki:** Dado que mencionaste temas de **SCADA y Post-Quantum**, podrías añadir una sección en el futuro sobre cómo protegerías este inventario farmacéutico contra ataques externos.

¿Te gustaría que personalice alguna sección técnica adicional, como la configuración específica de   
