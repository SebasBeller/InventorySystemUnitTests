import unittest
from unittest.mock import MagicMock
from Modelo.G_catalogo.Catalogo import Catalogo
from Modelo.G_inventario.Producto import Producto


class TestCatalogo(unittest.TestCase):

    def setUp(self):
        self.catalogo=Catalogo()

    def tearDown(self):
        self.catalogo=None

    def test_agregar_cero_productos_al_catalogo(self):
            self.catalogo.agregar_productos([])
            self.assertEqual(self.catalogo.productos,[])

    def test_agregar_un_producto_al_catalogo(self):
            producto = MagicMock(spec=Producto)
            self.catalogo.agregar_productos([producto])
            self.assertIn(producto, self.catalogo.productos)

    def test_obtener_lista_productos_vacia(self):
        self.catalogo.productos=[]
        self.assertEqual(self.catalogo.obtener_productos(),[])

    def test_obtener_lista_productos(self):
        producto = MagicMock(spec=Producto)
        self.catalogo.productos=[producto]
        self.assertEqual(self.catalogo.obtener_productos(),[producto])

    def test_get_str_catalogo(self):
        producto = MagicMock(spec=Producto)
        producto.get_nombre.return_value = 'Laptop'
        producto.get_modelo.return_value = 'HP'
        producto.get_precio.return_value = 20
        producto.get_stock.return_value = 5
        self.catalogo.productos=[producto]
        cadena_catalogo= (
            "Nombre: Laptop\n"
            "Modelo: HP\n"
            "Precio: 20\n"
            "Estado: Disponible\n\n"
        )
        self.assertEqual(str(self.catalogo),cadena_catalogo)

    def test_get_str_catalogo_con_producto_agotado(self):
        producto = MagicMock(spec=Producto)
        producto.get_nombre.return_value = 'Laptop'
        producto.get_modelo.return_value = 'HP'
        producto.get_precio.return_value = 20
        producto.get_stock.return_value = 0
        self.catalogo.productos=[producto]
        cadena_catalogo= (
            "Nombre: Laptop\n"
            "Modelo: HP\n"
            "Precio: 20\n"
            "Estado: Agotado\n\n"
        )
        self.assertEqual(str(self.catalogo),cadena_catalogo)

    def test_get_str_catalogo_con_cero_productos(self):
        self.assertEqual(str(self.catalogo),"")