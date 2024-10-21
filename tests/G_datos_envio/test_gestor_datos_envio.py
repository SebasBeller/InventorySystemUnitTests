import unittest
from unittest.mock import MagicMock
from Modelo.G_datos_envio.GestorDatosEnvio import GestorDatosEnvio
from Modelo.G_datos_envio.DatoEnvio import DatoEnvio
from Modelo.G_datos_envio.TablaDatosEnvio import TablaDatosEnvio


class TestGestorDatosEnvio(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorDatosEnvio()
        self.gestor.tabla_datos_envio = MagicMock(spec=TablaDatosEnvio)

    def tearDown(self):
        self.gestor=None

    def test_verificar_datos_campos_completos(self):
        resultado = self.gestor.verificar_datos_envio("Juan", "Calle 123", "Ciudad", "12345", "Pais")
        self.assertTrue(resultado)

    def test_verificar_datos_campo_pais_vacio(self):
        resultado = self.gestor.verificar_datos_envio("Juan", "Calle 123", "Ciudad", "12345", "")
        self.assertFalse(resultado)

    def test_verificar_datos_campo_codigo_postal_vacio(self):
        resultado = self.gestor.verificar_datos_envio("Juan", "Calle 123", "Ciudad", "", "")
        self.assertFalse(resultado)

    def test_verificar_datos_campo_ciudad_vacio(self):
        resultado = self.gestor.verificar_datos_envio("Juan", "Calle 123", "", "", "")
        self.assertFalse(resultado)

    def test_verificar_datos_campo_direccion_vacio(self):
        resultado = self.gestor.verificar_datos_envio("Juan", "", "", "", "")
        self.assertFalse(resultado)

    def test_verificar_datos_campo_nombre_vacio(self):
        resultado = self.gestor.verificar_datos_envio("", "", "", "", "")
        self.assertFalse(resultado)

    def test_recibir_datos_agregar_datos_envio_exitoso(self):
        self.gestor.tabla_datos_envio.agregar_dato_envio.return_value = True
        resultado = self.gestor.recibir_datos_agregar_datos_envio("Juan", "Calle 124", "Ciudad", "12345", "Pais")
        self.assertTrue(resultado)

    def test_recibir_datos_agregar_datos_envio_fallido(self):
        resultado = self.gestor.recibir_datos_agregar_datos_envio("", "Calle 124", "Ciudad", "12345", "Pais")
        self.assertFalse(resultado)

    def test_obtener_datos_envio(self):
        resultado = self.gestor.obtener_datos_envio()
        self.assertIsNotNone(resultado)

