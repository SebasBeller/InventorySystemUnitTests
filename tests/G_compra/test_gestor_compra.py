import unittest
from unittest.mock import MagicMock,patch
from Modelo.G_carrito.TablaCarritos import TablaCarritos
from Modelo.G_carrito.Carrito import Carrito
from Modelo.G_compra.Ticket import Ticket
from Modelo.G_compra import TablaCompra,GestorCompra
from Modelo.G_usuario.Session import Session

class TestGestorCompra(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorCompra()
        self.gestor.tabla_carritos = MagicMock(spec=TablaCarritos)
        self.gestor.session = MagicMock(spec=Session)
        self.gestor.tabla = MagicMock(spec=TablaCompra)
        self.mock_carrito = MagicMock(spec=Carrito)
        self.gestor.tabla_carritos.carritos=[self.mock_carrito]
        self.productos_carrito = [
            {'modelo': 'Producto1', 'cantidad': 2, 'precio': 100},
        ]

    def tearDown(self):
        self.gestor=None
        self.mock_carrito=None
        self.productos_carrito=None

    @patch("Modelo.G_compra.Ticket.Ticket")
    @patch("Modelo.G_compra.GestorCompra.GestorCompra.obtener_carrito")
    def test_solicitud_compra_exitoso(self, mock_obtener_carrito,mock_ticket):
        mock_obtener_carrito.return_value = self.mock_carrito
        mock_ticket.return_value = MagicMock(spec=Ticket)
        mock_obtener_carrito.obtener_carrito.return_value = self.productos_carrito
        resultado = self.gestor.solicitud_compra()
        self.assertTrue(resultado)

    @patch("Modelo.G_compra.Ticket.Ticket")
    @patch("Modelo.G_compra.GestorCompra.GestorCompra.obtener_carrito")
    def test_solicitud_compra_sin_productos(self, mock_carrito, mock_ticket):
        mock_carrito.return_value = self.mock_carrito
        mock_ticket.return_value = MagicMock(spec=Ticket)
        mock_carrito.obtener_carrito.return_value = []
        resultado = self.gestor.solicitud_compra()
        self.assertTrue(resultado)

    @patch("Modelo.G_compra.Ticket.Ticket")
    @patch("Modelo.G_compra.GestorCompra.GestorCompra.obtener_carrito")
    def test_solicitud_compra_fallido(self, mock_carrito, mock_ticket):
        mock_carrito.return_value = None
        resultado = self.gestor.solicitud_compra()
        self.assertFalse(resultado)

