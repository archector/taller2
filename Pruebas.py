'''
Created on 19/1/2015

@author: Hector Goncalves
@author: Daniel Zeait
'''
import unittest
from funciones import calcularMonto 

class Test_Calcular_Monto(unittest.TestCase):

    #cuando las fechas son iguales
    def test_fechas_iguales(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:00"),None,"pass")
        
    #cuando la fecha de salida es menor que la fecha de entrada    
    def test_salida_menor_entrada(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 11 20 18:13"),None,"pass")
    
    #cuando una reservacion supera el maximo de dias posibles para reservar
    def test_max_dias_reserva(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 24 18:00"),None,"pass")
    
    #cuando una reservacion está por debajo del limite de tiempo minimo para reservar
    def test_min_tiempo_reserva(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:13"),None,"pass")
    
    #monto minimo a pagar por una reservacion de tiempo minimo 
    def test_montoMin_tiempoMin(self):
        self.assertEquals(calcularMonto("2015 12 20 10:00" ,"2015 12 20 10:15"),2,"pass")

    #monto maximo a pagar por una reservacion de tiempo minimo 
    def test_montoMax_tiempoMin(self):
        self.assertEquals(calcularMonto("2015 12 20 18:00" ,"2015 12 20 18:15"),4,"pass")
        
    #monto minimo a pagar por una reservacion de tiempo maximo 
    def test_montoMin_tiempoMax(self):
        self.assertEquals(calcularMonto("2015 12 20 00:00" ,"2015 12 23 00:00"),217,"pass")
    
    #monto maximo a pagar por una reservacion de tiempo maximo 
    def test_montoMax_tiempoMax(self):
        self.assertEquals(calcularMonto("2015 12 20 00:00" ,"2015 12 23 23:59"),274,"pass")
        
