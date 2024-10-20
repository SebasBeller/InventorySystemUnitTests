import unittest
from Modelo.G_pago.TarjetaBancaria import TarjetaBancaria

class TestTarjetaBancaria(unittest.TestCase):

    def setUp(self):
       self.datosTarjeta=TarjetaBancaria(12345,"11/09/2024",123)

    def test_getNumero(self):
        self.assertEqual(self.datosTarjeta.get_numero(),12345)

    def test_getFechaVencimiento(self ):
        self.assertEqual(self.datosTarjeta.get_fecha_vencimiento(),"11/09/2024")

    def test_getCvv(self):
        self.assertEqual(self.datosTarjeta.get_cvv(),123)

    def test_setNumero(self):
        numero_tarjeta = "000123"
        self.datosTarjeta.set_numero(numero_tarjeta)
        self.assertEqual(self.datosTarjeta.get_numero(), numero_tarjeta)

    def test_setFechaVenicimiento(self):
        fecha_vencimiento= "11/10/2025"
        self.datosTarjeta.set_fecha_vencimiento(fecha_vencimiento)
        self.assertEqual(self.datosTarjeta.get_fecha_vencimiento(),fecha_vencimiento)

    def test_setCvv(self):
        numero_cvv=456
        self.datosTarjeta.set_cvv(numero_cvv)
        self.assertEqual(self.datosTarjeta.get_cvv(),numero_cvv)
