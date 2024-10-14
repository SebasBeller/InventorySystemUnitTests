import unittest
from Modelo.G_pago.TarjetaCredito import TarjetaCredito

class TestTarjetaCredito(unittest.TestCase):

    def setUp(self):
        self.tarjeta = TarjetaCredito("1234567890123456", "12/25", "123")


    def test_getTipo(self):
        self.assertEqual(self.tarjeta.get_tipo(), "Credito")
