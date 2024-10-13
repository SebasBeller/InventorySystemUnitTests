import unittest
from Modelo.G_compra import Ticket

class TestTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(1,"1/1/2024")

    def test_agregar_producto(self):
        self.ticket.agregar_producto("modelo",1,50)
        self.assertNotEqual(self.ticket.productos,[])

    def test_obtener_total(self):
        self.ticket.agregar_producto("ModeloA",1,200)
        self.ticket.agregar_producto("modelob",2,10)
        total=self.ticket.obtener_total()
        self.assertEqual(total,220)

    def test_obtener_total_vacio(self):
        self.ticket.agregar_producto("",0,0)
        total=self.ticket.obtener_total()
        self.assertEqual(total,0)

    def test_obtener_productos(self):
        self.ticket.agregar_producto("ModeloA",1,200)
        productos=self.ticket.obtener_productos()
        self.assertEqual(productos,[{'cantidad':1,'modelo':'ModeloA','precio':200}])

    def test_regresa_ticket_formato_srt(self):
        self.ticket=Ticket(1,"1/1/2024")
        self.ticket.agregar_producto("ModeloA",1,200)
        self.assertEqual(str(self.ticket),"Ticket: 1 - 1/1/2024 - 200")

