import unittest

from Modelo.G_ganancia.TablaGanancia import TablaGanancia
from unittest.mock import MagicMock

from Modelo.G_ganancia import Reporte


class TestTablaGanancia(unittest.TestCase):
    def setUp(self):
        self.tabla_ganancia = TablaGanancia()
        self.reporte=MagicMock(spec=Reporte)
        self.tabla_ganancia.reportes=[self.reporte]

    def tearDown(self):
        self.tabla_ganancia.reportes=None
        self.reporte=None
        self.tabla_ganancia=None

    def test_obtener_total_tabla_ganancia_con_reporte(self):
        self.reporte.obtener_total.return_value=200
        self.assertEqual(self.tabla_ganancia.obtener_total(),200)

    def test_obtener_total_tabla_ganancia_sin_reporte(self):
        self.tabla_ganancia.reportes=[]
        self.assertEqual(self.tabla_ganancia.obtener_total(),0)

    def test_agregar_reporte(self):
        nuevo_reporte=MagicMock(spec=Reporte)
        self.tabla_ganancia.agregar_reporte(nuevo_reporte)
        self.assertEqual(len(self.tabla_ganancia.reportes),2)

    def test_obtener_reporte(self):
        self.assertListEqual(self.tabla_ganancia.obtener_reportes(),[self.reporte])


