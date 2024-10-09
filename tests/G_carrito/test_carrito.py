import unittest
from Modelo.G_carrito.Carrito import Carrito
from unittest.mock import patch
from unittest.mock import MagicMock

class TestCarrito(unittest.TestCase):

    def setUp(self):
        self.carrito = Carrito()
        self.carrito.productos = [
            {"nombre": "Producto1", "precio": 100},
            {"nombre": "Producto2", "precio": 200},
            {"nombre": "Producto3", "precio": 300}
        ]

    def test_eliminar_producto_existe(self):
        self.carrito.eliminar_producto("Producto1")
        self.assertNotIn({"nombre": "Producto1", "precio": 100}, self.carrito.productos)

    def test_eliminar_producto_no_existe(self):
        self.carrito.eliminar_producto("ProductoInexistente")
        self.assertEqual(len(self.carrito.productos), 3)

    def test_eliminar_producto_con_nombre_mayusculas_minusculas(self):
        self.carrito.eliminar_producto("producto1")
        self.assertNotIn({"nombre": "Producto1", "precio": 100}, self.carrito.productos)

    def test_obtener_total_con_productos(self):
        self.carrito.productos = [
            {"precio": 100, "cantidad": 2},
            {"precio": 200, "cantidad": 1}
        ]
        total = self.carrito.obtener_total()
        self.assertEqual(total, 400)

    def test_obtener_total_sin_productos(self):
        self.carrito.productos = []
        total = self.carrito.obtener_total()
        self.assertEqual(total, 0)

    @patch('builtins.print')
    def test_mostrar_carrito_con_un_producto(self, mock_print):
        self.carrito.productos = [
            {"nombre": "Producto1", "precio": 100, "cantidad": 2}
        ]

        self.carrito.mostrar_carrito()
        mock_print.assert_any_call("\n=== Carrito ===\n")
        mock_print.assert_any_call("Producto: Producto1 Precio: 100 Cantidad: 2")
        mock_print.assert_any_call("\nTotal: 200")

    @patch('builtins.print')
    def test_mostrar_carrito_con_dos_productos(self, mock_print):
        self.carrito.productos = [
            {"nombre": "Producto1", "precio": 100, "cantidad": 2},
            {"nombre": "Producto2", "precio": 200, "cantidad": 1}
        ]

        self.carrito.mostrar_carrito()
        mock_print.assert_any_call("\n=== Carrito ===\n")
        mock_print.assert_any_call("Producto: Producto1 Precio: 100 Cantidad: 2")
        mock_print.assert_any_call("Producto: Producto2 Precio: 200 Cantidad: 1")
        mock_print.assert_any_call("\nTotal: 400")

    @patch('builtins.print')
    def test_mostrar_carrito_vacio(self, mock_print):
        self.carrito.productos = []
        self.carrito.mostrar_carrito()
        mock_print.assert_called_once_with("\nCarrito vacío")

    def test_agregar_producto(self):
        self.carrito.productos = []
        producto = MagicMock()
        producto.get_modelo.return_value = "ModeloX"
        producto.get_nombre.return_value = "ProductoX"
        producto.get_precio.return_value = 100.0

        self.carrito.agregar_producto(producto, "4")  # Agregamos el producto con cantidad "4"

        self.assertEqual(len(self.carrito.productos), 1)  # Debe ser 1 producto
        self.assertEqual(self.carrito.productos[0]["modelo"], "ModeloX")
        self.assertEqual(self.carrito.productos[0]["nombre"], "ProductoX")
        self.assertEqual(self.carrito.productos[0]["precio"], 100.0)
        self.assertEqual(self.carrito.productos[0]["cantidad"], 4)

    def test_obtener_carrito(self):
        carrito_obtenido = self.carrito.obtener_carrito()
        self.assertEqual(carrito_obtenido, self.carrito.productos)

    def test_limpiar_carrito(self):
        self.carrito.limpiar_carrito()
        self.assertEqual(self.carrito.productos, [])  # El carrito debe estar vacío
