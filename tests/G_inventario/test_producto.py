import unittest
from Modelo.G_inventario.Producto import  Producto

class TestProducto(unittest.TestCase):
    def setUp(self):
        self.producto = Producto(
            nombre="Collar de Perlas",
            modelo="2024",
            marca="Perlas Elegantes",
            stock="Disponible",
            material="Perlas naturales",
            color="Blanco",
            piedra="Perla",
            precio=250
        )

    def tearDown(self):
        self.producto = None

    def test_get_nombre(self):
        self.assertEqual(self.producto.get_nombre(), "Collar de Perlas")

    def test_get_modelo(self):
        self.assertEqual(self.producto.get_modelo(), "2024")

    def test_get_marca(self):
        self.assertEqual(self.producto.get_marca(), "Perlas Elegantes")

    def test_get_stock(self):
        self.assertEqual(self.producto.get_stock(), "Disponible")

    def test_get_material(self):
        self.assertEqual(self.producto.get_material(), "Perlas naturales")

    def test_get_color(self):
        self.assertEqual(self.producto.get_color(), "Blanco")

    def test_get_piedra(self):
        self.assertEqual(self.producto.get_piedra(), "Perla")

    def test_get_precio(self):
        self.assertEqual(self.producto.get_precio(), 250)

    def test_set_stock(self):
        self.producto.set_stock("No Disponible")
        self.assertEqual(self.producto.get_stock(), "No Disponible")
    def test_get_str(self):
        cadena_producto=(
            "Nombre: Collar de Perlas\n"
            "Modelo: 2024\n"
            "Marca: Perlas Elegantes\n"
            "Stock: Disponible\n"
            "Material: Perlas naturales\n"
            "Color: Blanco\n"
            "Piedra: Perla\n"
            "Precio: 250"
        )
        self.assertEqual(str(self.producto), cadena_producto)


