import unittest
from Modelo.G_datos_envio import TablaDatosEnvio,DatoEnvio
from unittest.mock import MagicMock, patch  
from Modelo.G_usuario.Session import Session

class TestTablaDatosEnvio(unittest.TestCase):

    def setUp(self):
        self.tabla_datos_envio = TablaDatosEnvio()
        self.tabla_datos_envio.session = MagicMock(spec=Session)
        self.dato_envio_mock = MagicMock(spec=DatoEnvio)
        self.tabla_datos_envio.tabla_datos_envio[1] = [self.dato_envio_mock]

    def tearDown(self):
        self.tabla_datos_envio=None
        self.dato_envio_mock=None


    def test_agregar_dato_envio_de_usuario_con_cero_envios(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2
        dato_envio_mock = MagicMock(spec=DatoEnvio)
        agrego_correctamente=self.tabla_datos_envio.agregar_dato_envio(dato_envio_mock)
        self.assertTrue(agrego_correctamente)

    def test_agregar_dato_envio_de_usuario_con_envios_existentes(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        dato_envio_mock = MagicMock(spec=DatoEnvio)
        agrego_correctamente=self.tabla_datos_envio.agregar_dato_envio(dato_envio_mock)
        self.assertTrue(agrego_correctamente)

    def test_obtener_datos_envio_usuario_con_datos(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        datos_obtenidos = self.tabla_datos_envio.obtener_datos_envio()
        self.assertNotEqual(datos_obtenidos,[])

    def test_obtener_datos_envio_usuario_sin_datos(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2
        datos_obtenidos = self.tabla_datos_envio.obtener_datos_envio()
        self.assertEqual(datos_obtenidos, [])

    def test_modificar_pais(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("pais", "Nuevo País", 0)
        self.dato_envio_mock.set_pais.assert_called_once_with("Nuevo País")

    def test_modificar_con_tipo_dato_invalido(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        result = self.tabla_datos_envio.modificar_dato("tipo_invalido", "dato", 0)
        self.assertTrue(result)

    def test_modificar_cp(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("cp", "12345", 0)
        self.dato_envio_mock.set_codigo_postal.assert_called_once_with("12345")

    def test_modificar_ciudad(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("ciudad", "Nueva Ciudad", 0)
        self.dato_envio_mock.set_ciudad.assert_called_once_with("Nueva Ciudad")

    def test_modificar_direccion(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("direccion", "Nueva Dirección", 0)
        self.dato_envio_mock.set_direccion.assert_called_once_with("Nueva Dirección")

    def test_modificar_nombre(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.tabla_datos_envio.modificar_dato("nombre", "Nuevo Nombre", 0)
        self.dato_envio_mock.set_nombre.assert_called_once_with("Nuevo Nombre")

    def test_tiene_datos_envio(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.assertTrue(self.tabla_datos_envio.tiene_datos_envio())

    def test_no_tiene_datos_envio(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2
        self.assertFalse(self.tabla_datos_envio.tiene_datos_envio())

    def test_eliminar_dato_envio(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.assertTrue(self.tabla_datos_envio.eliminar_dato(0))

    def test_eliminar_dato_envio_con_indice_superior_al_tamanio(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.assertFalse(self.tabla_datos_envio.eliminar_dato(5))

    def test_eliminar_dato_envio_con_indice_negativo(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 1
        self.assertFalse(self.tabla_datos_envio.eliminar_dato(-1))

    def test_eliminar_dato_envio_sin_envios_del_usuario(self):
        self.tabla_datos_envio.session.obtener_id_usuario.return_value = 2
        self.assertFalse(self.tabla_datos_envio.eliminar_dato(0))