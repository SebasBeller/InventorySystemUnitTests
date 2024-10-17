import unittest
from Modelo.G_usuario.Administrador import Administrador

class TestAdministrador(unittest.TestCase):

    def setUp(self):
        self.administrador = Administrador("Pepito","pepito@gmail.com","1234",1)

    def tearDown(self):
        self.administrador = None

    def test_get_puesto(self):
        self.assertEqual(self.administrador.get_puesto(),"CEO")

    def test_set_puesto(self):
        self.administrador.set_puesto("CTO")
        self.assertEqual(self.administrador.puesto,"CTO")


