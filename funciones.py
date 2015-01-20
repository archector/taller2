# -*- coding: utf-8 -*

'''
Created on Jan 18, 2015

@author: Hector Goncalves
@author: Daniel Zeait
'''
from datetime import datetime#Libreria que que maneja fechas y horas 

if __name__ == '__main__':
    pass

#Lista de Fechas de inicio de la reservación
fechaIniRes = "2015 12 20 18:00"   

#Lista de Fechas en las que se termina la reservación
fechaFinRes= "2015 12 21 17:59"   

#Diccionario con las tarifas asociadas a etapa diurna o nocturna
tarifa_diurna = 2
tarifa_nocturna = 4
hora_extra = 0

#funcion que determina la tarifa a ser usada dependiendo la hora de entrada
def hallarTarifa(horaI):
    if horaI.hour < 18:
        tarifa = tarifa_diurna
    else:
        tarifa = tarifa_nocturna
    return tarifa

#funcion que dada dos fechas verifica que sean correctas
def validar_fechas(fecha1,fecha2):

    if fecha2 < fecha1:
        es_valida_fecha = False
    else:
        es_valida_fecha = True
    
    return es_valida_fecha


def validar_dias(fecha1,fecha2):    
    #caso en que la reserva sea por mas de tres dias
    if ((fecha2.day - fecha1.day) <= 3) and (fecha2.month == fecha1.month) and (fecha2.year == fecha1.year):
        es_valida_dias = True
    else:
        es_valida_dias = False

    if ((fecha2.day - fecha1.day) == 0) and (fecha2.month != fecha1.month):
        es_valida_dias = True
        
    if (fecha2.year == fecha1.year) and (fecha2.month > fecha1.month) and (fecha1.day - fecha2.day >= 28) and (fecha1.month in(1,3,5,7,8,10,12)):
        es_valida_dias = True

    if (fecha2.year == fecha1.year) and  (fecha2.month > fecha1.month) and (fecha1.day - fecha2.day >= 27) and (fecha1.month in(4,6,9,11)):
        es_valida_dias = True

    if (fecha2.year - fecha1.year == 1) and (fecha1.day - fecha2.day >= 28) and (fecha1.month == 12) and (fecha2.month == 1):
        es_valida_dias = True
        
    if (fecha2.year == fecha1.year) and  (fecha2.month > fecha1.month) and (fecha1.day - fecha2.day >= 25) and (fecha1.month == 2):
        es_valida_dias = True
        
    return es_valida_dias
    
def validar_minutos(fecha1,fecha2):
    #caso en que la reserva sea por menos de 30 minutos
    if ((fecha2.minute - fecha1.minute) < 15) and (fecha2.month == fecha1.month) and (fecha2.day == fecha1.day):
        es_valida_min = False
    else:
        es_valida_min = True    
    return es_valida_min

#funcion que calcula el monto a pagar por una reservacion de estacionamiento
def calcularMonto(fechaInicio, fechaFin):
    
    #convertimos los str en fechas
    horaIni = datetime.strptime(fechaInicio, "%Y %m %d %H:%M")
    horaFin = datetime.strptime(fechaFin, "%Y %m %d %H:%M")    
    
    #validamos las fechas dadas
    valida_fecha = validar_fechas(horaIni,horaFin)
    valida_dias = validar_dias(horaIni,horaFin)
    valida_min = validar_minutos(horaIni,horaFin) 
    
    if valida_fecha == False:
        print("La fecha de salida debe ser mayor a la fecha de entrada")

    if valida_dias == False:
        print("La reserva no puede ser por mas de tres dias")

    if valida_min == False:
        print("La reserva no puede ser menor a 15 minutos")
        
    if (valida_fecha == True) and (valida_dias == True) and (valida_min == True) and (valida_min == True): 
            
        #calculamos la tarifa a usar
        tarifa = hallarTarifa(horaIni)
        
        #en caso de que la reserva dure mas de un dia
        if (horaFin.month > horaIni.month) and (horaIni.day - horaFin.day >= 28) and (horaIni.month in(1,3,5,7,8,10,12)):
            total_dias = 31-(horaIni.day - horaFin.day)
        elif (horaFin.month > horaIni.month) and (horaIni.day - horaFin.day >= 27) and (horaIni.month in(4,6,9,11)):
            total_dias = 30-(horaIni.day - horaFin.day)
        elif (horaFin.month > horaIni.month) and (horaIni.day - horaFin.day >= 25) and (horaIni.month == 2):
            total_dias = 28-(horaIni.day - horaFin.day)
        elif (horaFin.month == 1) and (horaIni.day - horaFin.day >= 28) and (horaIni.month == 12):
            total_dias = 31-(horaIni.day - horaFin.day)    
        else:
            total_dias = horaFin.day - horaIni.day
        
        #calculamos el total de dias que dura la reservacion
        monto_dias = (total_dias) * ((12*tarifa_diurna) + (12*tarifa_nocturna))
        
        #calculamos el monto a pagar por horas
        total_horas = horaFin.hour - horaIni.hour
        monto_horas = total_horas * tarifa
        
        #calculamos el monto a pagar por fracciones de hora
        total_min = abs(horaFin.minute - horaIni.minute)
          
        if total_min != 0:
            hora_extra = tarifa
        else:
            hora_extra = 0
        
        #en caso de manejar dos tarifas por un mismo dia
        if horaIni.hour < 18 and horaFin.hour > 18:
            monto1 = (18 - horaIni.hour) * tarifa_diurna
            monto2 = (horaFin.hour-18) * tarifa_nocturna
    
            monto_total = monto_dias + monto1 + monto2 + hora_extra
    
        elif (total_min >= 15) and (total_horas == 0):
            monto_total = tarifa
            
        else:   
            monto_total = monto_dias + monto_horas + hora_extra
        
        return monto_total

monto = calcularMonto(fechaIniRes,fechaFinRes)
print("El monto a pagar es")
print(monto)
#print(calcularMonto("2015 12 20 23:59" ,"2015 12 21 00:03"))