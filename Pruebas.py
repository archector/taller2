'''
Created on 19/1/2015

@author: Hector Goncalves
@author: Daniel Zeait
'''
import unittest
from funciones import calcularMonto 

class Test_Calcular_Monto(unittest.TestCase):

    def test_fechas_iguales(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:00"),None,"pass")
        
    def test_salida_menor_entrada(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 11 20 18:13"),None,"pass")
        
    def test_max_dias(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 24 18:00"),None,"pass")
        
    def test_min_tiempo(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:13"),None,"pass")

    def test_montoMin_tiempoMin(self):
        self.assertEquals(calcularMonto("2015 12 20 10:00" ,"2015 12 20 10:15"),2,"pass")

    def test_montoMax_tiempoMin(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:15"),4,"pass")
        
    def test_montoMin_tiempoMax(self):
        self.assertEquals(calcularMonto("2015 12 20 00:00" ,"2015 12 23 00:00"),216,"pass")
        
    def test_montoMax_tiempoMax(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 23 18:00"),216,"pass")
        
    def test_montoMin_23horas_59min(self):
        self.assertEquals(calcularMonto("2015 12 20 00:00" ,"2015 12 20 23:59"),58,"pass")
        
    def test_montoMax_23_horas_59min(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 21 17:59"),72,"pass")        
        
    def test_hora_incompleta(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:59"),4,"pass")
        
    