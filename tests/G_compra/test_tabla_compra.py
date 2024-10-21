import unittest

from Modelo.G_compra import Ticket
from Modelo.G_compra.TablaCompra import TablaCompra
from unittest.mock import MagicMock, patch


class testTablaCompra(unittest.TestCase):

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_agregar_nuevo_ticket_al_segundo_diccionario(self,mock_init_test):
        TablaCompra.init_test=mock_init_test
        self.tabla_compra=TablaCompra()
        self.tabla_compra.tickets=[{0:[MagicMock(spec=Ticket)]},
                                   {1:[MagicMock(spec=Ticket)]}]
        ticket=MagicMock(spec=Ticket)
        self.tabla_compra.agregar_ticket(ticket,1)
        self.assertIn(ticket,self.tabla_compra.tickets[1][1])

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_agregar_nuevo_ticket_al_primer_diccionario(self,mock_init_test):
        TablaCompra.init_test=mock_init_test
        self.tabla_compra=TablaCompra()
        self.tabla_compra.tickets=[{1:[MagicMock(spec=Ticket)]}]
        ticket=MagicMock(spec=Ticket)
        self.tabla_compra.agregar_ticket(ticket,1)
        self.assertIn(ticket,self.tabla_compra.tickets[0][1])

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_agregar_nuevo_ticket_con_nuevo_identificador(self,mock_init_test):
        TablaCompra.init_test=mock_init_test
        self.tabla_compra=TablaCompra()
        self.tabla_compra.tickets=[{1:[MagicMock(spec=Ticket)]}]
        ticket=MagicMock(spec=Ticket)
        identificador=0
        self.tabla_compra.agregar_ticket(ticket,identificador)
        self.assertIn(ticket,self.tabla_compra.tickets[1][identificador])

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_agregar_tickets_lista_vacia_de_tickets(self,mock_init_test):
        TablaCompra.init_test=mock_init_test
        self.tabla_compra=TablaCompra()
        ticket=MagicMock(spec=Ticket)
        identificador=1
        self.tabla_compra.agregar_ticket(ticket,identificador)
        self.assertEqual(len(self.tabla_compra.tickets),1)

    def test_inicializar_tickets(self):
        self.tabla_compra=TablaCompra()
        self.tabla_compra.init_test()
        self.assertNotEqual(self.tabla_compra.tickets,[])

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_obtener_lista_ticket_un_identificador(self,mock_init_test ):
        TablaCompra.init_test = mock_init_test
        self.tabla_compra=TablaCompra()
        ticket1=MagicMock(spec= Ticket)
        ticket2=MagicMock(spec= Ticket)
        self.tabla_compra.tickets=[
            {1:[ticket1]},
            {2:[ticket2]}
        ]
        result=self.tabla_compra.obtener_tickets()
        self.assertEqual(len(result),2)

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_obtener_tikect_sin_identificador(self,mock_init_test):
        TablaCompra.init_test = mock_init_test
        self.tabla_compra=TablaCompra()
        self.tabla_compra.tickets=[{}]
        result=self.tabla_compra.obtener_tickets()
        self.assertEqual(len(result),0)

    @patch('Modelo.G_compra.TablaCompra.TablaCompra.init_test')
    def test_obtener_tikects_sin_tickets_en_compra(self,mock_init_test):
        TablaCompra.init_test = mock_init_test
        self.tabla_compra=TablaCompra()
        self.tabla_compra.tickets=[]
        result=self.tabla_compra.obtener_tickets()
        self.assertEqual(len(result),0)