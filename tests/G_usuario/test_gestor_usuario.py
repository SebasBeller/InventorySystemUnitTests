import unittest
from unittest.mock import MagicMock,patch

from Modelo.G_usuario import TablaUsuarios, Autenticacion, Miembro, Administrador
from Modelo.G_usuario.GestorUsuario import GestorUsuario


class TestGestorUsuario(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorUsuario()
        self.gestor.tabla_usuarios=MagicMock(spec=TablaUsuarios)
        self.gestor.autenticacion=MagicMock(spec=Autenticacion)
        mock_miembro = MagicMock(spec=Miembro)
        mock_miembro.get_nombre.return_value = "Juan"
        mock_miembro.get_correo.return_value = "correo@ejemplo.com"
        mock_miembro.get_contrasena.return_value = "222"
        mock_admin = MagicMock(spec=Administrador)
        mock_admin.get_nombre.return_value = "Pedro"
        mock_admin.get_correo.return_value = "correo2@ejemplo.com"
        mock_admin.get_contrasena.return_value = "111"
        self.miembro = mock_miembro
        self.administrador = mock_admin

    def tearDown(self):
        self.gestor = None

    def test_preparar_datos_usuario_miembro(self):
        miembro_diccionario=self.gestor.preparar_datos_usuario(self.miembro)
        self.assertIsNotNone(miembro_diccionario)

    def test_preparar_datos_usuario_admin(self):
        miembro_diccionario=self.gestor.preparar_datos_usuario(self.administrador)
        self.assertIsNotNone(miembro_diccionario)

    @patch("Modelo.G_usuario.GestorUsuario.GestorUsuario.set_id")
    def test_recibir_datos_registro(self, mock):
        mock.return_value = 1
        self.gestor.tabla_usuarios.obtener_usuario.return_value = None
        self.assertTrue(self.gestor.recibir_datos_registro_usuario("Mario", "mario2@ejemplo.com","555"))

    @patch("Modelo.G_usuario.GestorUsuario.GestorUsuario.set_id")
    def test_recibir_datos_registro_usuario_registrado(self, mock):
        mock.return_value = 1
        self.gestor.tabla_usuarios.obtener_usuario.return_value = self.administrador
        self.assertFalse(self.gestor.recibir_datos_registro_usuario("Pedro", "correo2@ejemplo.com", "111"))

    @patch("Modelo.G_usuario.GestorUsuario.GestorUsuario.seleccion_miembro_eliminar")
    def test_eliminar_cuenta_miembro(self,mock_miembro_eliminar):
        self.gestor.tabla_usuarios.obtener_miembros.return_value = [self.miembro, self.administrador]
        mock_miembro_eliminar.return_value=1
        self.gestor.tabla_usuarios.eliminar_cuenta.return_value=[self.administrador]
        self.assertNotIn(self.miembro,self.gestor.solicitud_eliminar_cuenta_miembro())

    @patch("Modelo.G_usuario.GestorUsuario.GestorUsuario.seleccion_miembro_eliminar")
    def test_eliminar_cuenta_miembro_regresar(self, mock_miembro_eliminar):
        self.gestor.tabla_usuarios.obtener_miembros.return_value = []
        mock_miembro_eliminar.return_value = 0
        self.assertFalse(self.gestor.solicitud_eliminar_cuenta_miembro())