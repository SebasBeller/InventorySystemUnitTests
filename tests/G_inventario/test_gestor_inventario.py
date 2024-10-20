import unittest
from unittest.mock import MagicMock

from scipy.special import special

from Modelo.G_inventario.GestorInventario import GestorInventario
from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import Aretes, Producto, Collares


class TestGestorInventario(unittest.TestCase):

    def setUp(self):
        self.gestor=GestorInventario()
        self.gestor.Inventario=MagicMock(spec=Inventario)
        self.producto=MagicMock(spec=Aretes)
        self.producto.get_nombre.return_value='Aretes de Perla'
        self.gestor.Inventario.productos_catalogo=[self.producto]

    def tearDown(self):
        self.gestor=None
        self.producto=None

    def test_actualizar_stock(self):
        self.gestor.actualizar_stock("Aretes de Perla",20)
        self.producto.set_stock.assert_called_once_with(20)

    def test_actualizar_stock_nombre_producto_inexistente(self):
        self.gestor.actualizar_stock("Collares de Perla",20)
        self.producto.set_stock.assert_not_called()

    def test_actualizar_stock_sin_productos(self):
        self.gestor.Inventario.productos_catalogo=[]
        self.gestor.actualizar_stock("",0)
        self.producto.set_stock.assert_not_called()

    def test_obtener_inventario(self):
        self.gestor.Inventario.obtener_inventario.return_value=self.gestor.Inventario.productos_catalogo
        self.assertIsNotNone(self.gestor.obtener_inventario())

    def test_buscar_producto_inventario(self):
        self.gestor.Inventario.buscar_producto.return_value=self.producto
        self.assertEqual(self.gestor.buscar_producto("Aretes de Perla"),self.producto)

    def test_agregar_producto(self):
        producto=MagicMock(spec=Collares)
        self.gestor.agregar_producto(producto)
        self.gestor.Inventario.agregar_producto.assert_called_once_with(producto)
