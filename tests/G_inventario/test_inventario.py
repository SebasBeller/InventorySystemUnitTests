import unittest
from Modelo.G_inventario.Inventario import Inventario
from unittest.mock import MagicMock
from unittest.mock import patch

from Modelo.G_inventario.Producto import Producto


class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()
        self.producto=MagicMock(spec=Producto)
        self.producto.nombre="Aretes de plata"
        self.producto.stock=10


    def tearDown(self):
        self.inventario = None

    def test_agregar_agrega_producto_existente(self):
        self.inventario.productos={"Aretes de plata":0}
        self.inventario.agregar_producto(self.producto)
        self.assertIn(self.producto,self.inventario.productos_catalogo)

    def test_agregar_nuevo_producto(self):
        self.inventario.agregar_producto(self.producto)
        self.assertIn(self.producto, self.inventario.productos_catalogo)

    def test_obtener_producto_de_lista_por_nombre(self):
        self.inventario.productos_catalogo=[MagicMock(spec=Producto),MagicMock(spec=Producto)]
        self.inventario.productos_catalogo[0].get_nombre.return_value="Pulsera de oro"
        self.inventario.productos_catalogo[0].get_modelo.return_value="Modelo"
        self.inventario.productos_catalogo[1].get_nombre.return_value="Pulsera de Plata"
        resp=self.inventario.obtener_producto("pulsera de plata")
        self.assertIsNotNone(resp)

    def test_obtener_producto_de_lista_por_modelo(self):
        self.inventario.productos_catalogo = [MagicMock(spec=Producto)]
        self.inventario.productos_catalogo[0].get_nombre.return_value = "Pulsera de oro"
        self.inventario.productos_catalogo[0].get_modelo.return_value = "Modelo"
        resp = self.inventario.obtener_producto("modelo")
        self.assertIsNotNone(resp)

    def test_obtener_producto_sin_coincidencias_en_identificador(self):
        self.inventario.productos_catalogo = [MagicMock(spec=Producto)]
        self.inventario.productos_catalogo[0].get_nombre.return_value = "Pulsera de oro"
        self.inventario.productos_catalogo[0].get_modelo.return_value = "Modelo"
        resp = self.inventario.obtener_producto("Ninguno")
        self.assertIsNone(resp)

    def test_obtener_producto_de_lista_vacia(self):
        resp = self.inventario.obtener_producto("Niguno")
        self.assertIsNone(resp)

    @patch('builtins.print')
    def test_eliminar_producto_existente(self, mock_print):
        self.inventario.productos = {"mochila": 0}
        self.inventario.eliminar_producto("mochila")
        mock_print.assert_called_with("\nProducto eliminado correctamente.")

    @patch('builtins.print')
    def test_eliminar_inexistente(self,mock_print):
        self.inventario.productos = {}
        self.inventario.eliminar_producto("X")
        mock_print.assert_called_with("\nEl producto no existe en el inventario.")

    def test_buscar_existente(self):
        self.inventario.productos = {"laptop": 0}
        resp=self.inventario.buscar_producto("laptop")
        self.assertEqual(resp,"laptop: 0")

    def test_buscar_inexistente(self):
        self.inventario.productos = {}
        resp=self.inventario.buscar_producto("laptop")
        self.assertEqual(resp,"\nProducto no encontrado.")

    def test_actualizar_stock_producto_existente(self):
            self.inventario.productos = {"laptop": 0}
            self.inventario.actualizar_stock("laptop",10)
            self.assertEqual(self.inventario.productos,{"laptop":10})

    @patch('builtins.print')
    def test_actualizar_stock_producto_inexistente(self,mock_print):
            self.inventario.productos = {}
            self.inventario.actualizar_stock("laptop",5)
            mock_print.assert_called_with("\nEl producto no existe en el inventario.")

    def test_obtener_lista_productos(self):
            self.assertIsNotNone(self.inventario.obtener_lista_productos())

    def test_obtener_inventario_de_productos(self):
            self.assertIsNotNone(self.inventario.obtener_inventario())

    def test_inicializar_inventario(self):
            self.inventario.inicializar_inventario()
            self.assertNotEqual(self.inventario.productos_catalogo,[])
