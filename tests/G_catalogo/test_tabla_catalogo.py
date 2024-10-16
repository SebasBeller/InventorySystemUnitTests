import unittest
from codecs import IncrementalEncoder
from unittest.mock import patch, MagicMock
from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes, Producto
from Modelo.G_catalogo.TablaCatalogo import TablaCatalogo
from Modelo.G_inventario.Inventario import  Inventario


class TestTablaCatalogo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.productos_mock = [
            MagicMock(spec=Dijes), MagicMock(spec=Pulseras), MagicMock(spec=Piercings),
            MagicMock(spec=Anillos), MagicMock(spec=Collares), MagicMock(spec=Aretes)
        ]
        producto=MagicMock(spec=Producto)
        producto.nombre = "Collar Elegante"
        producto.modelo = "CE2024"
        producto.marca = "Pandora"
        producto.stock = 5
        producto.material = "Plata"
        producto.color = "Plateado"
        producto.piedra = "Zafiro"
        producto.precio = 150.00
        cls.producto = producto

    @classmethod
    def tearDownClass(cls):
        cls.productos_mock = None

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_dijes_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[0]]
        resultado = tabla_catalogo.obtener_catalogo("Dijes")
        self.assertEqual(resultado, tabla_catalogo.productos_inventario)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_dijes_catalogo_sin_dijes(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [MagicMock()]
        resultado = tabla_catalogo.obtener_catalogo("Dijes")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_ninguno_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[0]]
        resultado = tabla_catalogo.obtener_catalogo("Ninguno")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_pulseras_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[1]]
        resultado = tabla_catalogo.obtener_catalogo("Pulseras")
        self.assertEqual(resultado, tabla_catalogo.productos_inventario)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_pulseras_del_catalogo_sin_pulseras(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [MagicMock()]
        resultado = tabla_catalogo.obtener_catalogo("Pulseras")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_piercings_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[2]]
        resultado = tabla_catalogo.obtener_catalogo("Piercings")
        self.assertEqual(resultado, tabla_catalogo.productos_inventario)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_piercings_del_catalogo_sin_piercings(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [MagicMock()]
        resultado = tabla_catalogo.obtener_catalogo("Piercings")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_anillos_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[3]]
        resultado = tabla_catalogo.obtener_catalogo("Anillos")
        self.assertEqual(resultado, tabla_catalogo.productos_inventario)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_anillos_del_catalogo_sin_anillos(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [MagicMock()]
        resultado = tabla_catalogo.obtener_catalogo("Anillos")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_collares_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[4]]
        resultado = tabla_catalogo.obtener_catalogo("Collares")
        self.assertEqual(resultado, tabla_catalogo.productos_inventario)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_collares_del_catalogo_sin_collares(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [MagicMock()]
        resultado = tabla_catalogo.obtener_catalogo("Collares")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_aretes_del_catalogo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.productos_mock[5]]
        resultado = tabla_catalogo.obtener_catalogo("Aretes")
        self.assertEqual(resultado, tabla_catalogo.productos_inventario)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_aretes_del_catalogo_sin_aretes(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [MagicMock()]
        resultado = tabla_catalogo.obtener_catalogo("Aretes")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_obtener_productos_del_catalogo_sin_tipo(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = []
        resultado = tabla_catalogo.obtener_catalogo("-")
        self.assertEqual(resultado, [])

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_buscar_producto_por_piedra(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        self.producto.get_piedra.return_value="Zafiro"
        tabla_catalogo.productos_inventario = [self.producto]
        resultado = tabla_catalogo.buscar_producto("Zafiro")
        self.assertIn(self.producto, resultado)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_buscar_producto_por_ningun_criterio(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = [self.producto]
        resultado = tabla_catalogo.buscar_producto("Ninguno")
        self.assertEqual([], resultado)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_buscar_producto_por_color(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        self.producto.get_color.return_value = "Plateado"
        tabla_catalogo.productos_inventario = [self.producto]
        resultado = tabla_catalogo.buscar_producto("Plateado")
        self.assertIn(self.producto, resultado)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_buscar_producto_por_material(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        self.producto.get_material.return_value = "Plata"
        tabla_catalogo.productos_inventario = [self.producto]
        resultado = tabla_catalogo.buscar_producto("Plata")
        self.assertIn(self.producto, resultado)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_buscar_producto_por_nombre(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        self.producto.get_material.return_value = "Collar Elegante"
        tabla_catalogo.productos_inventario = [self.producto]
        resultado = tabla_catalogo.buscar_producto("Collar Elegante")
        self.assertIn(self.producto, resultado)

    @patch('Modelo.G_catalogo.TablaCatalogo.TablaCatalogo.obtener_productos_inventario')
    def test_buscar_producto_catalogo_sin_productos(self, mock_obtener_productos):
        TablaCatalogo.obtener_productos_inventario = mock_obtener_productos
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.productos_inventario = []
        resultado = tabla_catalogo.buscar_producto("-")
        self.assertEqual([], resultado)

    @patch('Modelo.G_inventario.Inventario.Inventario.obtener_inventario')
    def test_obtener_productos_inventario(self,mock_obtener_inventario):
        mock_obtener_inventario.return_value = self.productos_mock
        tabla_catalogo = TablaCatalogo()
        tabla_catalogo.obtener_productos_inventario()
        self.assertNotEqual(len(tabla_catalogo.productos_inventario),0)