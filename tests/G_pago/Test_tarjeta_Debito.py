import unittest
from Modelo.G_pago.TarjetaDebito import TarjetaDebito

class TestTarjetaDebito(unittest.TestCase):

    def setUp(self):
        self.tarjeta = TarjetaDebito("1234567890123456", "12/25", "123")


    def test_getTipo(self):
        self.assertEqual(self.tarjeta.get_tipo(), "Debito")