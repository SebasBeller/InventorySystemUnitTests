import unittest
from Modelo.G_compra import Ticket

class TestTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(1,"1/1/2024")
    def test_agregar_ticket(self):
        self.ticket.agregar_producto("modelo",1,50)
        self.assertNotEqual(self.ticket.productos,[])