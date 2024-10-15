import unittest
from unittest.mock import MagicMock

from Modelo.G_carrito import Carrito
from Modelo.G_carrito.TablaCarritos import TablaCarritos

class TestTablaCarritos(unittest.TestCase):

    def setUp(self):
        self.tabla_carritos = TablaCarritos()
        self.carrito_mock = MagicMock(spec=Carrito)

    def test_guardar_carrito(self):

        self.assertEqual(len(self.tabla_carritos.carritos), 0)
        self.tabla_carritos.guardar_carrito(self.carrito_mock)
        self.assertEqual(len(self.tabla_carritos.carritos), 1)
        self.assertEqual(self.tabla_carritos.carritos[0], self.carrito_mock)
        
    def test_obtener_ultimo_carrito_con_carritos(self):
        carrito_mock1 = MagicMock(spec=Carrito)
        carrito_mock2 = MagicMock(spec=Carrito)
        self.tabla_carritos.guardar_carrito(carrito_mock1)
        self.tabla_carritos.guardar_carrito(carrito_mock2)
        ultimo_carrito = self.tabla_carritos.obtener_ultimo_carrito()
        self.assertEqual(ultimo_carrito, carrito_mock2)

    def test_obtener_ultimo_carrito_sin_carritos(self):
        ultimo_carrito = self.tabla_carritos.obtener_ultimo_carrito()
        self.assertIsNone(ultimo_carrito)