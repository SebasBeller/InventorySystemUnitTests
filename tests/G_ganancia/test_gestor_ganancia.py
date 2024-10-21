import unittest
from unittest.mock import MagicMock, patch

from Modelo.G_compra import Ticket
from Modelo.G_ganancia import TablaGanancia, Reporte
from Modelo.G_ganancia.GestorGanancia import GestorGanancia


class TestGestorGanancia(unittest.TestCase):

    def setUp(self):
        self.gestor=GestorGanancia()
        self.gestor.tabla=MagicMock(spec=TablaGanancia)

    def tearDown(self):
        self.gestor=None

    @patch("Modelo.G_compra.TablaCompra.TablaCompra.obtener_tickets")
    def test_prepara_tickects_lista_tickets_mas_de_cinco(self,mock_tabla_obtener_tickets):
        tickets=[
            MagicMock(spec=Ticket),
            MagicMock(spec=Ticket),
            MagicMock(spec=Ticket),
            MagicMock(spec=Ticket),
            MagicMock(spec=Ticket),
            MagicMock(spec=Ticket)
        ]
        mock_tabla_obtener_tickets.return_value=tickets
        self.assertListEqual(self.gestor.prepara_tickets(),tickets[1:])

    @patch("Modelo.G_compra.TablaCompra.TablaCompra.obtener_tickets")
    def test_prepara_tickects_lista_tickets_menos_de_cinco(self, mock_tabla_obtener_tickets):
        tickets = [
            MagicMock(spec=Ticket)
        ]
        mock_tabla_obtener_tickets.return_value = tickets
        self.assertListEqual(self.gestor.prepara_tickets(), tickets)

    def test_consultar_ultimo_reporte_con_reportes(self):
        reportes = [
            MagicMock(spec=Reporte),
            MagicMock(spec=Reporte)
        ]
        self.gestor.tabla.obtener_reportes.return_value=reportes
        self.assertEqual(self.gestor.consultar_reportes(), reportes[-1])

    def test_consultar_ultimo_reporte_sin_reportes(self):
            reportes = []
            self.gestor.tabla.obtener_reportes.return_value = reportes
            self.assertEqual(self.gestor.consultar_reportes(), [])

    @patch("Modelo.G_ganancia.GestorGanancia.GestorGanancia.prepara_tickets")
    def test_consultar_generar_reporte(self,mock_tickets):
        mock_tickets.return_value=[]
        self.assertIsNotNone(self.gestor.generar_reporte())
