import unittest
from unittest.mock import MagicMock

from Modelo.G_usuario import TablaUsuarios, Usuario
from Modelo.G_usuario.Autenticacion import Autenticacion

class TestAutenticacion(unittest.TestCase):

    def setUp(self):
        tabla_usuarios=MagicMock(spec=TablaUsuarios)
        self.autenticacion = Autenticacion(tabla_usuarios)
        self.autenticacion.tabla_usuarios.validar_credenciales.return_value = MagicMock(spec=Usuario)

    def tearDown(self):
        self.autenticacion = None

    def test_validar_credenciales_credenciales_validos(self):
        self.assertTrue(self.autenticacion.validacion_credenciales("pepito@gmail.com","1234"))

    def test_validar_credenciales_credenciales_invalidos(self):
        self.autenticacion.tabla_usuarios.validar_credenciales.return_value = None
        self.assertFalse(self.autenticacion.validacion_credenciales("pepito@gmail.com","9876"))
