import unittest
from unittest.mock import MagicMock,patch

from scipy.special import special

from Modelo.G_pago import TablaPago, TarjetaDebito, TarjetaCredito
from Modelo.G_pago.GestorPago import GestorPago


class TestGestorPago(unittest.TestCase):

    def setUp(self):
        self.gestor=GestorPago()
        self.gestor._GestorPago__tabla_pago=MagicMock(spec=TablaPago)

    def tearDown(self):
        self.gestor=None

    def test_validar_datos_con_datos_validos(self):
        sonValidos=self.gestor.validar_datos(numero="4444444444444444",fecha_vencimiento="10/25",cvv="123")
        self.assertTrue(sonValidos)

    def test_validar_datos_cvv_invalido(self):
        sonValidos = self.gestor.validar_datos(numero="4444444444444444", fecha_vencimiento="10/25", cvv="1")
        self.assertFalse(sonValidos)

    def test_validar_datos_fecha_vencimiento_invalida(self):
        sonValidos = self.gestor.validar_datos(numero="4444444444444444", fecha_vencimiento="1/25", cvv="")
        self.assertFalse(sonValidos)

    def test_validar_datos_numero_invalido(self):
        sonValidos = self.gestor.validar_datos(numero="44", fecha_vencimiento="", cvv="")
        self.assertFalse(sonValidos)

    @patch("Modelo.G_pago.GestorPago.GestorPago.validar_datos")
    @patch("Modelo.G_pago.TarjetaCredito")
    def test_recibir_datos_bancarios_tarjeta_credito(self,mock_tarjeta_credito,mock_validar_datos):
        mock_validar_datos.return_value=True
        mock_tarjeta_credito.return_value=MagicMock(spec=TarjetaCredito)
        datos_recibidos = self.gestor.recibir_datos_bancarios_agregar(numero="1111111111111111",fecha_vencimiento="10/25",cvv="123",tipo_tarjeta="credito")
        self.assertTrue(datos_recibidos)

    @patch("Modelo.G_pago.GestorPago.GestorPago.validar_datos")
    @patch("Modelo.G_pago.TarjetaDebito")
    def test_recibir_datos_bancarios_tarjeta_debito(self,mock_tarjeta_debito,mock_validar_datos):
        mock_validar_datos.return_value=True
        mock_tarjeta_debito.return_value=MagicMock(spec=TarjetaDebito)
        datos_recibidos = self.gestor.recibir_datos_bancarios_agregar(numero="1111111111111111",fecha_vencimiento="10/25",cvv="123",tipo_tarjeta="debito")
        self.assertTrue(datos_recibidos)

    @patch("Modelo.G_pago.GestorPago.GestorPago.validar_datos")
    def test_recibir_datos_bancarios_invalidos(self,mock_validar_datos):
        mock_validar_datos.return_value=False
        datos_recibidos = self.gestor.recibir_datos_bancarios_agregar(numero="1111111111111111",fecha_vencimiento="10/25",cvv="123",tipo_tarjeta="")
        self.assertFalse(datos_recibidos)

    def test_obtener_tarjetas(self):
        self.gestor._GestorPago__tabla_pago.obtener_tarjetas.return_value=[MagicMock(spec=TarjetaDebito)]
        self.assertIsNotNone(self.gestor.solicitud_obtener_tarjetas_bancarias())