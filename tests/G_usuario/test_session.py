import unittest
from unittest.mock import MagicMock

from Modelo.G_usuario import  Usuario, Session

class TestSession(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = Session()
        cls.usuario=MagicMock(spec=Usuario)

    @classmethod
    def tearDownClass(cls):
        cls.session = None

    def test_iniciar_sesion(self):
        self.session.iniciar_sesion(self.usuario)
        self.assertIsNotNone(self.session.usuario_autenticado)

    def test_cerrar_sesion(self):
        self.session.cerrar_sesion()
        self.assertIsNone(self.session.usuario_autenticado)


