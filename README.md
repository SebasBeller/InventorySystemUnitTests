# Joyeria-PIS-I
# Proyecto de Pruebas Unitarias para Gestión de Inventarios

## Descripción

Este proyecto consiste en la implementación de pruebas unitarias para una aplicación de gestión de inventarios desarrollada en Python. Se utilizaron las herramientas **PyUnit** (unittest) y **Coverage** para medir el porcentaje de cobertura de código y garantizar la calidad del software. El objetivo principal es mejorar la mantenibilidad y estabilidad del código mediante la detección temprana de errores en los módulos críticos de la aplicación.

## Características

- Pruebas unitarias usando **PyUnit** (unittest)
- Medición de la cobertura de código con **Coverage**
- Cobertura de más del 90% en los módulos críticos del sistema (Inventario, Catálogos, Carrito, Compra, Datos de envío y Pago)
- Cobertura de más del 80% en módulos relativamente importantes (Ganancias y Usuario)

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto localmente:

### Requisitos previos

Asegúrate de tener instalados los siguientes elementos en tu entorno:

- Python 3.x
- `pip` para la gestión de paquetes

### Pasos de instalación

1. **Clonar el repositorio:**

     ```bash
     git clone https://github.com/SebasBeller/InventorySystemUnitTests.git
2. **Instalar Coverage:**
 
      ```bash
      pip install coverage

### Pasos para ejecutar la Cobertura de código
**Para medir la cobertura del código utilizando Coverage, sigue estos pasos:**

     python -m coverage run --rcfile=.coveragerc -m unittest discover -s tests

**Genera el reporte de cobertura:**

     python -m coverage report  --rcfile=.coveragerc
**También puedes generar un informe en HTML para visualizarlo en el navegador:**
      
     python -m coverage html --rcfile=.coveragerc
**Ver el reporte de cobertura en HTML:**

Abre el archivo htmlcov/index.html en tu navegador para ver un reporte detallado de la cobertura.

### Uso
El sistema está diseñado para probar de manera eficiente todos los módulos de una aplicación de inventarios.
