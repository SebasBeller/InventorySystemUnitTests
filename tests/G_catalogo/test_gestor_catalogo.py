import unittest
from unittest.mock import MagicMock,patch
from Modelo.G_catalogo import TablaCatalogo, GestorCatalogo, Catalogo
from Modelo.G_inventario.Producto import Aretes


class TestGestorCatalogo(unittest.TestCase):

    def setUp(self):
        mock_tabla_catalogo = MagicMock(spec=TablaCatalogo)
        self.gestor = GestorCatalogo()
        self.gestor.tabla_catalogo = mock_tabla_catalogo

    def tearDown(self):
        self.gestor = None

    @patch("Modelo.G_catalogo.Catalogo.Catalogo")
    def test_recibir_dato_catalogo(self, mock_catalogo):
        mock_catalogo.return_value = MagicMock(spec=Catalogo)
        self.gestor.tabla_catalogo.obtener_catalogo.return_value=[MagicMock(spec=Aretes)]
        self.assertIsNotNone(self.gestor.recibir_dato_catalogo("Aretes"))

    @patch("Modelo.G_catalogo.Catalogo.Catalogo")
    def test_recibir_dato_busqueda(self, mock_catalogo):
        mock_catalogo.return_value = MagicMock(spec=Catalogo)
        producto=MagicMock(spec=Aretes)
        producto.nombre="Aretes de Plata"
        self.gestor.tabla_catalogo.buscar_producto.return_value=[producto]
        self.assertIsNotNone(self.gestor.recibir_dato_busqueda("Aretes de Plata"))


