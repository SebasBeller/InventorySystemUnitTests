import unittest
from Modelo.G_inventario.Inventario import Inventario
from unittest.mock import MagicMock
from unittest.mock import patch

class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()

    def tearDown(self):
        self.inventario = None

    def test_agregar_tc1(self):
        producto=MagicMock()
        producto.nombre="Aretes de plata"
        self.inventario.productos={"Aretes de plata":0}
        self.inventario.agregar_producto(producto)
        self.assertIn(producto,self.inventario.productos_catalogo)

    def test_agregar_tc2(self):
        producto = MagicMock()
        producto.nombre = "ProductoX"
        self.inventario.agregar_producto(producto)
        self.assertIn(producto, self.inventario.productos_catalogo)

    def test_obtener_producto_tc1(self):
        self.inventario.productos_catalogo=[MagicMock(),MagicMock()]
        self.inventario.productos_catalogo[0].get_nombre.return_value="X"
        self.inventario.productos_catalogo[0].get_modelo.return_value="M"
        self.inventario.productos_catalogo[1].get_nombre.return_value="Y"
        resp=self.inventario.obtener_producto("y")
        self.assertIsNotNone(resp)

    def test_obtener_producto_tc2(self):
        self.inventario.productos_catalogo = [MagicMock()]
        self.inventario.productos_catalogo[0].get_nombre.return_value = "X"
        self.inventario.productos_catalogo[0].get_modelo.return_value = "M"
        resp = self.inventario.obtener_producto("m")
        self.assertIsNotNone(resp)

    def test_obtener_producto_tc3(self):
        self.inventario.productos_catalogo = [MagicMock()]
        self.inventario.productos_catalogo[0].get_nombre.return_value = "X"
        self.inventario.productos_catalogo[0].get_modelo.return_value = "M"
        resp = self.inventario.obtener_producto("z")
        self.assertIsNone(resp)

    def test_obtener_producto_tc4(self):
        resp = self.inventario.obtener_producto("z")
        self.assertIsNone(resp)

    @patch('builtins.print')  # Mockear la función print
    def test_eliminar_producto_tc1(self, mock_print):
        self.inventario.productos = {"mochila": 0}
        self.inventario.eliminar_producto("mochila")
        mock_print.assert_called_with("\nProducto eliminado correctamente.")

    @patch('builtins.print')
    def test_eliminar_tc2(self,mock_print):
        self.inventario.productos = {}
        self.inventario.eliminar_producto("X")
        mock_print.assert_called_with("\nEl producto no existe en el inventario.")

    def test_buscar_tc1(self):
        self.inventario.productos = {"laptop": 0}
        resp=self.inventario.buscar_producto("laptop")
        self.assertEqual(resp,"laptop: 0")

    def test_buscar_tc2(self):
        self.inventario.productos = {}
        resp=self.inventario.buscar_producto("laptop")
        self.assertEqual(resp,"\nProducto no encontrado.")

    def test_actualizar_stock_tc1(self):
            self.inventario.productos = {"laptop": 0}
            self.inventario.actualizar_stock("laptop",10)
            self.assertEqual(self.inventario.productos,{"laptop":10})

    @patch('builtins.print')
    def test_actualizar_stock_tc2(self,mock_print):
            self.inventario.productos = {}
            self.inventario.actualizar_stock("laptop",5)
            mock_print.assert_called_with("\nEl producto no existe en el inventario.")

    def test_obtener_lista_productos_tc1(self):
            self.assertIsNotNone(self.inventario.obtener_lista_productos())

    def test_obtener_inventario_tc1(self):
            self.assertIsNotNone(self.inventario.obtener_inventario())

    def test_inicializar_inventario_tc1(self):
            self.inventario.inicializar_inventario()
            self.assertNotEqual(self.inventario.productos_catalogo,[])
