import unittest
from Modelo.G_inventario.Inventario import Inventario
from unittest.mock import MagicMock
class TestInventario(unittest.TestCase):

    def test_agregar_tc1(self):
        Inventario.inicializar_inventario=MagicMock()
        self.inventario=Inventario()
        producto=MagicMock()
        producto.nombre="Aretes de plata"
        self.inventario.productos={"Aretes de plata":0}
        self.inventario.agregar_producto(producto)
        self.assertIn(producto,self.inventario.productos_catalogo)

    def test_agregar_tc2(self):
        Inventario.inicializar_inventario=MagicMock()
        self.inventario=Inventario()
        producto = MagicMock()
        producto.nombre = "ProductoX"
        self.inventario.agregar_producto(producto)
        self.assertIn(producto, self.inventario.productos_catalogo)

    def test_obtener_producto_tc1(self):
        Inventario.inicializar_inventario=MagicMock()
        self.inventario=Inventario()
        self.inventario.productos_catalogo=[MagicMock(),MagicMock()]
        self.inventario.productos_catalogo[0].get_nombre.return_value="X"
        self.inventario.productos_catalogo[0].get_modelo.return_value="M"
        self.inventario.productos_catalogo[1].get_nombre.return_value="Y"
        resp=self.inventario.obtener_producto("y")
        self.assertIsNotNone(resp)

    def test_obtener_producto_tc2(self):
        Inventario.inicializar_inventario = MagicMock()
        self.inventario = Inventario()
        self.inventario.productos_catalogo = [MagicMock()]
        self.inventario.productos_catalogo[0].get_nombre.return_value = "X"
        self.inventario.productos_catalogo[0].get_modelo.return_value = "M"
        resp = self.inventario.obtener_producto("m")
        self.assertIsNotNone(resp)

    def test_obtener_producto_tc3(self):
        Inventario.inicializar_inventario = MagicMock()
        self.inventario = Inventario()
        self.inventario.productos_catalogo = [MagicMock()]
        self.inventario.productos_catalogo[0].get_nombre.return_value = "X"
        self.inventario.productos_catalogo[0].get_modelo.return_value = "M"
        resp = self.inventario.obtener_producto("z")
        self.assertIsNone(resp)

    def test_obtener_producto_tc4(self):
        Inventario.inicializar_inventario = MagicMock()
        self.inventario = Inventario()
        resp = self.inventario.obtener_producto("z")
        self.assertIsNone(resp)
