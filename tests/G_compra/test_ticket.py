import unittest
from Modelo.G_compra import Ticket

class TestTicket(unittest.TestCase):
  
    def setUp(self):
        self.ticket = Ticket(1,"1/1/2024")
        self.ticket.productos=[
            {"modelo":"modeloA","cantidad":1,"precio":200},
            {"modelo": "modeloB", "cantidad": 2, "precio": 10}
        ]
        
    def tearDown(self):
        self.ticket=None

    def test_agregar_producto(self):
        producto={"modelo":"modeloC","cantidad":1,"precio":50}
        self.ticket.agregar_producto(**producto)
        self.assertIn(producto,self.ticket.productos)

    def test_obtener_total(self):
        total=self.ticket.obtener_total()
        self.assertEqual(total,220)

    def test_obtener_total_vacio(self):
        self.ticket.productos=[]
        total=self.ticket.obtener_total()
        self.assertEqual(total,0)

    def test_obtener_productos(self):
        productos=self.ticket.obtener_productos()
        self.assertNotEqual(productos,[])

    def test_regresa_ticket_formato_srt(self):
        self.assertEqual(str(self.ticket),"Ticket: 1 - 1/1/2024 - 220")


