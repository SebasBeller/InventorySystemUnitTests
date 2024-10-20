import unittest
from unittest.mock import MagicMock,patch
from Modelo.G_carrito.GestorCarrito import GestorCarrito
from Modelo.G_carrito.Carrito import Carrito
from Modelo.G_carrito.TablaCarritos import TablaCarritos
from Modelo.G_inventario.Producto import Producto


class TestGestorCarrito(unittest.TestCase):

    def setUp(self):
        mock_carrito = MagicMock(spec=Carrito)
        mock_tabla_carritos = MagicMock(spec=TablaCarritos)
        self.gestor = GestorCarrito()
        self.gestor.carrito = mock_carrito
        self.gestor.tabla_carritos = mock_tabla_carritos

    def tearDown(self):
        del self.gestor


    @patch("Modelo.G_inventario.Inventario.Inventario.obtener_producto")
    def test_agregar_producto_exitoso(self,mock_obtener_producto):
        mock_obtener_producto.return_value = MagicMock(spec=Producto)
        resultado = self.gestor.agregar_producto("123", 2)
        self.assertTrue(resultado)

    @patch("Modelo.G_inventario.Inventario.Inventario.obtener_producto")
    def test_agregar_producto_fallido(self,mock_obtener_producto):
        mock_obtener_producto.return_value = None
        resultado = self.gestor.agregar_producto("123", 2)
        self.assertFalse(resultado)

    def test_eliminar_producto_exitoso(self):
        resultado = self.gestor.eliminar_producto("123")
        self.assertTrue(resultado)

    def test_eliminar_producto_fallido(self):
        self.gestor.carrito=None
        resultado = self.gestor.eliminar_producto("124")
        self.assertFalse(resultado)

    def test_obtener_total_carrito(self):
        self.gestor.carrito.obtener_total.return_value = 200
        self.assertEqual(self.gestor.obtener_total(),200)
