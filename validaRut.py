#Este programa calcula el digito verificador del rut
import re

#Esta función valida el formato de ingreso de datos
def validarDato(dato):
    patron = r'^\d{1,8}-[\dKk]$'
    return re.match(patron, dato)
    

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
        nroRut = dato.split('-')[0]
        dvRut = (dato[-1]).upper()
        print("verdadero" if validarRut(nroRut,dvRut) else "falso")
        break
    else:
        print("Ingrese un numero de rut válido")
