import unittest
from Modelo.G_datos_envio import TablaDatosEnvio
from unittest.mock import MagicMock, patch  # Asegúrate de importar patch
from Modelo.G_usuario.Session import Session

class TestTablaDatosEnvio(unittest.TestCase):

    def setUp(self):
        self.tabla_datos_envio = TablaDatosEnvio()
        self.tabla_datos_envio.session = MagicMock(spec=Session)

        self.dato_envio_mock = MagicMock()
        self.tabla_datos_envio.tabla_datos_envio[1] = [self.dato_envio_mock]

    def test_unica_instancia(self):
        instancia1 = TablaDatosEnvio()
        self.assertIsNotNone(instancia1)

    def test_misma_instancia_multiples_llamadas(self):
        instancia1 = TablaDatosEnvio()
        instancia2 = TablaDatosEnvio()
        self.assertIs(instancia1, instancia2)

    @patch('Modelo.G_datos_envio.DatoEnvio')
    def test_agregar_dato_envio_nuevo_usuario(self, MockDatoEnvio):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        dato_envio_mock = MockDatoEnvio.return_value
        self.tabla_datos_envio.agregar_dato_envio(dato_envio_mock)
        self.assertTrue(True)

    @patch('Modelo.G_datos_envio.DatoEnvio')
    def test_agregar_dato_envio_existente_usuario_vacio(self, MockDatoEnvio):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1

        self.tabla_datos_envio.tabla_datos_envio[1] = []

        dato_envio_mock = MockDatoEnvio.return_value
        self.tabla_datos_envio.agregar_dato_envio(dato_envio_mock)




    @patch('Modelo.G_datos_envio.DatoEnvio')
    def test_obtener_datos_envio_usuario_con_datos(self, MockDatoEnvio):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        dato_envio_mock = MockDatoEnvio.return_value
        self.tabla_datos_envio.tabla_datos_envio[1] = [dato_envio_mock]

        datos_obtenidos = self.tabla_datos_envio.obtener_datos_envio()

        self.assertEqual(datos_obtenidos, [dato_envio_mock])

    def test_obtener_datos_envio_usuario_sin_datos(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2

        datos_obtenidos = self.tabla_datos_envio.obtener_datos_envio()

        self.assertEqual(datos_obtenidos, [])

    def test_modificar_nombre(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("nombre", "Nuevo Nombre", 0)

        self.dato_envio_mock.set_nombre.assert_called_once_with("Nuevo Nombre")
    def test_modificar_direccion(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("direccion", "Nueva Dirección", 0)

        self.dato_envio_mock.set_direccion.assert_called_once_with("Nueva Dirección")
    def test_modificar_ciudad(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("ciudad", "Nueva Ciudad", 0)

        self.dato_envio_mock.set_ciudad.assert_called_once_with("Nueva Ciudad")
    def test_modificar_cp(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("cp", "12345", 0)

        self.dato_envio_mock.set_codigo_postal.assert_called_once_with("12345")

    def test_modificar_pais(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("pais", "Nuevo País", 0)

        self.dato_envio_mock.set_pais.assert_called_once_with("Nuevo País")

    def test_modificar_con_tipo_dato_invalido(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        result = self.tabla_datos_envio.modificar_dato("tipo_invalido", "dato", 0)

        self.assertTrue(result)

    def test_modificar_en_indice_inexistente(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        with self.assertRaises(IndexError):
            self.tabla_datos_envio.modificar_dato("nombre", "Nuevo Nombre", 1)  # Índice 1 no existe
    @patch('Modelo.G_datos_envio.DatoEnvio')
    def test_eliminar_dato_usuario_con_datos(self, MockDatoEnvio):

        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        dato_envio_mock = MockDatoEnvio.return_value
        self.tabla_datos_envio.tabla_datos_envio[1] = [dato_envio_mock]


        resultado = self.tabla_datos_envio.eliminar_dato(0)
        self.assertEqual(resultado, True)

    def test_eliminar_dato_indice_fuera_de_rango(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.tabla_datos_envio[1] = []

        resultado = self.tabla_datos_envio.eliminar_dato(2)
        self.assertEqual(resultado, False)

    def test_eliminar_dato_usuario_sin_datos(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2

        resultado = self.tabla_datos_envio.eliminar_dato(0)
        self.assertEqual(resultado, False)

    def test_tiene_datos_envio_usuario_con_datos(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.tabla_datos_envio[1] = ["dato1", "dato2"]
        resultado = self.tabla_datos_envio.tiene_datos_envio()
        self.assertEqual(resultado, True)

    @patch('Modelo.G_datos_envio.DatoEnvio')  # Mock para DatoEnvio.
    def test_tiene_datos_envio_usuario_con_datos(self, MockDatoEnvio):
        # Simulamos que el ID del usuario actual es 2.
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2

        # Simulamos que el usuario 2 tiene datos de envío.
        self.tabla_datos_envio.tabla_datos_envio[2] = [MockDatoEnvio.return_value]

        # Llamamos a la función.
        resultado = self.tabla_datos_envio.tiene_datos_envio()

        # Verificamos que el resultado sea True.
        self.assertEqual(resultado, True)

    @patch('Modelo.G_datos_envio.DatoEnvio')  # Mock para DatoEnvio.
    def test_tiene_datos_envio_usuario_sin_datos(self, MockDatoEnvio):
        # Simulamos que el ID del usuario actual es 2.
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = ""

        # Aseguramos que no haya datos de envío para el usuario 2.
        self.tabla_datos_envio.tabla_datos_envio[2] = []  # Esto puede ser innecesario si solo quieres que no exista la clave.

        # Llamamos a la función.
        resultado = self.tabla_datos_envio.tiene_datos_envio()

        # Verificamos que el resultado sea False.
        self.assertEqual(resultado, False)