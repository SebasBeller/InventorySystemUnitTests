import unittest
from Modelo.G_datos_envio import DatoEnvio
class TestDatoEnvio(unittest.TestCase):

    def setUp(self):
        self.dato_envio=DatoEnvio("Juan","Av.America","Cochabamba","12345","Bolivia")


    def test_get_nombre(self):

        self.assertEqual(self.dato_envio.get_nombre(),"Juan")

    def test_get_direccion(self):
        self.assertEqual(self.dato_envio.get_direccion(), "Av.America")

    def test_get_ciudad(self):
        self.assertEqual(self.dato_envio.get_ciudad(), "Cochabamba")

    def test_get_codigo_postal(self):
        self.assertEqual(self.dato_envio.get_codigo_postal(), "12345")

    def test_get_pais(self):
        self.assertEqual(self.dato_envio.get_pais(), "Bolivia")


    def test_set_nombre_valido(self):
        nuevo_nombre = "Carlos Rodríguez"
        self.dato_envio.set_nombre(nuevo_nombre)
        self.assertEqual(self.dato_envio.get_nombre(), nuevo_nombre)

    def test_set_nombre_invalido(self):
        with self.assertRaises(ValueError):
            self.dato_envio.set_nombre("")

    def test_set_direccion_valido(self):
        nueva_direccion = "Cala Cala"
        self.dato_envio.set_direccion(nueva_direccion)
        self.assertEqual(self.dato_envio.get_direccion(), nueva_direccion)

    def test_set_direccion_invalido(self):
        with self.assertRaises(ValueError):
            self.dato_envio.set_direccion("")

    def test_set_ciudad_valido(self):
        nueva_ciudad = "La Paz"
        self.dato_envio.set_ciudad(nueva_ciudad)
        self.assertEqual(self.dato_envio.get_ciudad(), nueva_ciudad)

    def test_set_ciudad_invalido(self):

        with self.assertRaises(ValueError):
            self.dato_envio.set_ciudad("")

    def test_set_codigo_postal_valido(self):
        datos_envio ="00123"
        self.dato_envio.set_codigo_postal(datos_envio)
        self.assertEqual(self.dato_envio.get_codigo_postal(), datos_envio)

    def test_set_codigo_postal_invalido(self):
         with self.assertRaises(ValueError):
             self.dato_envio.set_codigo_postal("")

    def test_set_pais_valido(self):
        dato_envio="Peru"
        self.dato_envio.set_pais(dato_envio)
        self.assertEqual(self.dato_envio.get_pais(),dato_envio)

    def test_set_pais_invalido(self):
        with self.assertRaises(ValueError):
            self.dato_envio.set_pais("")

    def test_str(self):
        resultado="Nombre: Juan\n Direccion:Av.America\n Ciudad:Cochabamba\n Codigo Postal:12345\n Pais:Bolivia"
        self.assertEqual(str(self.dato_envio),resultado)

