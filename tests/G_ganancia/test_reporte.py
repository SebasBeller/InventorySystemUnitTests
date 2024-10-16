import unittest
from Modelo.G_ganancia.Reporte import Reporte
from unittest.mock import MagicMock

from Modelo.G_compra import Ticket


class TestReporte(unittest.TestCase):

    def setUp(self):
        self.ticket=MagicMock(spec=Ticket)
        self.ticket.id_ticket=1
        self.ticket.fecha="1/1/2020"
        self.productos=[{"modelo":"modeloA","cantidad":2,"precio":200}]
        self.reporte = Reporte([self.ticket],1)


    def tearDown(self):
        self.reporte = None
        self.ticket=None

    def test_obtener_total_de_reporte_con_tickets(self):
        self.ticket.obtener_total.return_value=20
        self.assertEqual(self.reporte.obtener_total(),20)

    def test_obtener_total_de_reporte_con_cero_tickets(self):
        self.ticket.obtener_total.return_value=20
        self.reporte.tickets=[]
        self.assertEqual(self.reporte.obtener_total(),0)

    def test_obtener_string_de_reporte_con_compras_de_ticket(self):
        self.ticket.obtener_total.return_value=400
        self.ticket.obtener_productos.return_value=self.productos
        cadena_reporte=(
            "Ticket: 1, Fecha: 1/1/2020\n"
            "Modelo: modeloA, Cantidad: 2, Precio: 200\n"
            "Total: 400\n\n"
        )
        self.assertEqual(str(self.reporte),cadena_reporte)

    def test_obtener_string_de_reporte_sin_compras_de_ticket(self):
        self.ticket.obtener_total.return_value=0
        self.ticket.obtener_productos.return_value=[]
        cadena_reporte=(
            "Ticket: 1, Fecha: 1/1/2020\n"
            "Total: 0\n\n"
        )
        self.assertEqual(str(self.reporte),cadena_reporte)

    def test_obtener_string_de_reporte_sin_tickets(self):
        self.reporte.tickets=[]
        self.assertEqual(str(self.reporte),"")


