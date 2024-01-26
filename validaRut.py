#Este programa calcula el digito verificador del rut
import re

#Esta función valida el formato de ingreso de datos
def validarDato(dato):
    patron = r'^\d{1,8}-[\dKk]$'
    if re.match(patron, dato):
        return True
    else:
        return False

#Esta función valida el rut, ingresando como parámetros el número y el digito verificador
def validarRut(texto,dvRut):
    largo = len(texto)
    suma = pos = 0 
    while -pos < largo:
        for i in range (2,8):
            pos -=1
            suma += int(texto[pos]) * i
            if -pos  == largo:
                break
        i +=1
    d = 11 - (suma % 11)
    if d == 10:
        dv = "K"
    elif d == 11:
        dv = "0"
    else:
        dv = str(d)
        print((dv), (dvRut))
    return dv == dvRut


#PROGRAMA VALIDADOR DE RUT CHILENO

while True:
    dato = input("Ingrese rut: ")
    if validarDato(dato):
        print("verdadero" if validarRut(dato.split('-')[0],dato.split('-')[1].upper()) else "falso")
        break
    else:
        print("Ingrese un numero de rut válido")