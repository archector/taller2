'''
Created on Jan 17, 2015

@author: Hector Goncalves
@author: Daniel Zeait
'''
import datetime #Libreria que que maneja fechas y horas 

if __name__ == '__main__':
    pass

#Lista de Fechas de inicio de la reservación
fechaIniRes = ["2015 03 23 06:43","2015 04 14 05:55","2015 12 12 03:17"]    

#Lista de Fechas en las que se termina la reservación
fechaFinRes= []     

#Diccionario con las tarifas asociadas a etapa diurna o nocturna
tarifa = {
    "diurna" : "6.10",
    "nocturna" : "8.30"
}

#def calcularMonto(fechaInicio, horaInicio,fechaFin, horaFin, tarifa):

    

print(tarifa["diurna"])
for date in fechaIniRes:
    horaIni = datetime.datetime.strptime(date, "%Y %m %d %H:%M") 
    print(horaIni)