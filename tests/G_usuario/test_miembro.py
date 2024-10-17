import unittest
from Modelo.G_usuario.Miembro import Miembro

class TestMiembro(unittest.TestCase):

    def setUp(self):
        self.miembro = Miembro(
            "Julieta",
            "julieta@example.com",
            "password123",1
        )

    def tearDown(self):
        self.miembro=None


    def test_set_fecha_nacimiento(self):
        self.miembro.set_fecha_nacimiento("1990-05-15")
        self.assertEqual(self.miembro.fecha_nacimiento, "1990-05-15")


    def test_set_genero(self):
        self.miembro.set_genero("Femenino")
        self.assertEqual(self.miembro.genero, "Femenino")


    def test_set_pais(self):
        self.miembro.set_pais("México")
        self.assertEqual(self.miembro.pais, "México")
