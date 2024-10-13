import unittest
from unittest.mock import MagicMock
from Modelo.G_pago import TarjetaDebito
from Modelo.G_pago.TablaPago import TablaPago

class TestTablaPago(unittest.TestCase):

    def setUp(self):
        self.sistema_pagos = TablaPago()
        self.sistema_pagos.session = MagicMock()
        self.sistema_pagos._TablaPago__pagos = {}

    def tearDown(self):
        self.sistema_pagos= None

    def test_agregar_tarjeta_usuario_sin_tarjetas(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        tarjeta = "Tarjeta 1234"
        resultado = self.sistema_pagos.agregar_tarjeta(tarjeta)
        self.assertTrue(resultado)

    def test_agregar_tarjeta_usuario_con_tarjetas(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 2
        self.sistema_pagos._TablaPago__pagos[2] = ["Tarjeta existente"]
        tarjeta = "Tarjeta nueva 5678"
        resultado = self.sistema_pagos.agregar_tarjeta(tarjeta)
        self.assertEqual(resultado, True)

    def test_obtener_tarjetas_de_pago_existente(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 2
        self.sistema_pagos._TablaPago__pagos[2] = ["Tarjeta existente"]
        tarjeta=self.sistema_pagos.obtener_tarjetas()
        self.assertEqual(tarjeta, ["Tarjeta existente"])

    def test_obtener_tarjetas_de_usuario_sin_pagos(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        tarjeta=self.sistema_pagos.obtener_tarjetas()
        self.assertIsNone(tarjeta)

    def test_eliminar_tarjeta_usuario_con_tarjetas(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 2
        self.sistema_pagos._TablaPago__pagos[2] = [MagicMock(spec=TarjetaDebito)]
        resultado = self.sistema_pagos.eliminar_tarjeta(0)
        self.assertTrue(resultado)

    def test_eliminar_tarjeta_usuario_sin_tarjetas(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 2
        resultado = self.sistema_pagos.eliminar_tarjeta(0)
        self.assertFalse(resultado)

    def test_tiene_datos_pago_usuario_con_tarjetas(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        self.sistema_pagos._TablaPago__pagos[1] = [MagicMock(spec=TarjetaDebito)]
        resultado = self.sistema_pagos.tiene_datos_pago()
        self.assertTrue(resultado)

    def test_tiene_datos_pago_usuario_sin_tarjetas(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        self.sistema_pagos._TablaPago__pagos[2] = [MagicMock(spec=TarjetaDebito)]
        resultado = self.sistema_pagos.tiene_datos_pago()
        self.assertFalse(resultado)

    def test_modificar_fecha_vencimiento_de_tarjeta(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        self.sistema_pagos._TablaPago__pagos[1] = [MagicMock(spec=TarjetaDebito)]
        tipo="fecha_vencimiento"
        resultado = self.sistema_pagos.modificar_tarjeta(0,tipo,"11/10/2025")
        self.assertTrue(resultado)

    def test_modificar_cvv_de_tarjeta(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        self.sistema_pagos._TablaPago__pagos[1] = [MagicMock(spec=TarjetaDebito)]
        tipo="cvv"
        resultado = self.sistema_pagos.modificar_tarjeta(0,tipo,"123")
        self.assertTrue(resultado)

    def test_modificar_numero_de_tarjeta(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        self.sistema_pagos._TablaPago__pagos[1] = [MagicMock(spec=TarjetaDebito)]
        tipo="numero"
        resultado = self.sistema_pagos.modificar_tarjeta(0,tipo,"44444444")
        self.assertTrue(resultado)

    def test_modificar_tarjeta_de_usuario_sin_pagos(self):
        self.sistema_pagos.session.obtener_id_usuario.return_value = 1
        self.sistema_pagos._TablaPago__pagos[2] = [MagicMock(spec=TarjetaDebito)]
        tipo="-"
        resultado = self.sistema_pagos.modificar_tarjeta(0,tipo,"-")
        self.assertFalse(resultado)