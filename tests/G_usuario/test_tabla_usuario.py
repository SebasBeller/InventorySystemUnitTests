import unittest
from unittest.mock import MagicMock, patch

from Modelo.G_usuario import Usuario, Session, Miembro
from Modelo.G_usuario.TablaUsuarios import TablaUsuarios

class TestTablaUsuario(unittest.TestCase):

    def setUp(self):
        self.tablaUsuarios = TablaUsuarios()
        usuario=MagicMock(spec=Miembro)
        usuario.get_correo.return_value='pepito@example.com'
        usuario.get_contrasena.return_value='123'
        usuario.get_id.return_value=1
        self.tablaUsuarios.usuarios=[usuario]
        self.tablaUsuarios.session=MagicMock(spec=Session)
        self.tablaUsuarios.session.obtener_id_usuario.return_value=1

    def tearDown(self):
        self.tablaUsuarios=None

    def test_validar_credenciales_validos(self):
        usuario=self.tablaUsuarios.validar_credenciales('pepito@example.com','123')
        self.assertIsNotNone(usuario)

    def test_validar_credenciales_con_contrasena_invalida(self):
        usuario=self.tablaUsuarios.validar_credenciales('pepito@example.com','987')
        self.assertIsNone(usuario)

    def test_validar_credenciales_con_correo_invalida(self):
        usuario=self.tablaUsuarios.validar_credenciales('pepito2@example.com','123')
        self.assertIsNone(usuario)

    def test_validar_credenciales_sin_usuarios(self):
        self.tablaUsuarios.usuarios=[]
        usuario=self.tablaUsuarios.validar_credenciales('pepito@example.com','123')
        self.assertIsNone(usuario)


    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_pais_del_usuario(self,mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value=self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos=self.tablaUsuarios.modificar_dato_usuario(6,"Argentina")
        self.assertTrue(se_modificaron_los_datos)

    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_ningun_dato_del_usuario(self,mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value=self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos=self.tablaUsuarios.modificar_dato_usuario(7,"Nada")
        self.assertTrue(se_modificaron_los_datos)

    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_genero_del_usuario(self,mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value=self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos=self.tablaUsuarios.modificar_dato_usuario(5,"Masculino")
        self.assertTrue(se_modificaron_los_datos)

    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_fecha_nac_del_usuario(self,mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value=self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos=self.tablaUsuarios.modificar_dato_usuario(4,"1/1/2001")
        self.assertTrue(se_modificaron_los_datos)

    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_contrasena_del_usuario(self,mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value=self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos=self.tablaUsuarios.modificar_dato_usuario(3,"456")
        self.assertTrue(se_modificaron_los_datos)

    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_correo_del_usuario(self,mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value=self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos=self.tablaUsuarios.modificar_dato_usuario(2,"mario@example.com")
        self.assertTrue(se_modificaron_los_datos)

    @patch('Modelo.G_usuario.TablaUsuarios.TablaUsuarios.obtener_usuario_por_id')
    def test_modificar_correo_del_usuario(self, mock_obtener_usuario_por_id):
        mock_obtener_usuario_por_id.return_value = self.tablaUsuarios.usuarios[0]
        se_modificaron_los_datos = self.tablaUsuarios.modificar_dato_usuario(1, "mario")
        self.assertTrue(se_modificaron_los_datos)

    def test_obtener_miembros_lista_usuarios_con_un_miembro(self):
        self.assertEqual(self.tablaUsuarios.obtener_miembros(), self.tablaUsuarios.usuarios)

    def test_obtener_miembros_lista_miembros_con_un_usuario(self):
        self.tablaUsuarios.usuarios=[MagicMock(spec=Usuario)]
        self.assertEqual(self.tablaUsuarios.obtener_miembros(), [])

    def test_obtener_miembros_lista_sin_miembros(self):
        self.tablaUsuarios.usuarios = []
        self.assertEqual(self.tablaUsuarios.obtener_miembros(), [])

    def test_registrar_usuarios(self):
        usuario=MagicMock(spec=Usuario)
        self.tablaUsuarios.registrar_usuario(usuario)
        self.assertEqual(len(self.tablaUsuarios.usuarios), 2)

    def test_obtener_usuario_por_id_correcto(self):
        usuario=self.tablaUsuarios.obtener_usuario_por_id(1)
        self.assertIsNotNone(usuario)

    def test_obtener_usuario_por_id_incorrecto(self):
        usuario=self.tablaUsuarios.obtener_usuario_por_id(2)
        self.assertIsNone(usuario)

    def test_obtener_usuario_lista_usuarios_vacia(self):
        self.tablaUsuarios.usuarios=[]
        usuario=self.tablaUsuarios.obtener_usuario_por_id(1)
        self.assertIsNone(usuario)