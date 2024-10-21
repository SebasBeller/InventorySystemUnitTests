import unittest
from Modelo.G_usuario.Usuario import Usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario("Juan", "juan@example.com", "123", 1)

    def tearDown(self):
        self.usuario=None


    def test_set_nombre(self):
        self.usuario.set_nombre("Julieta")
        self.assertEqual(self.usuario.nombre, "Julieta")

    def test_set_correo(self):
        self.usuario.set_correo("julieta@example.com")
        self.assertEqual(self.usuario.correo, "julieta@example.com")

    def test_set_contrasena(self):
        self.usuario.set_contrasena("456")
        self.assertEqual(self.usuario.contrasena, "456")
