#Este programa calcula el digito verificador del rut
import re

#Esta función valida el formato de ingreso de datos

    # '''La función `validarDato` verifica si una cadena determinada coincide con el patrón de un número de
    # identificación chileno (RUT) válido.
    
    # Parameters
    # ----------
    # rut
    #     El parámetro "rut" es una cadena que representa un número de identificación chileno, comúnmente
    # conocido como "RUT" (Rol Único Tributario). Consta de una secuencia de dígitos seguida de un guión y
    # un dígito de verificación (que puede ser un dígito del 0 al 9).
    
    # Returns
    # -------
    #     el resultado de la función `re.match()`, que es un objeto de coincidencia si la `ruta` coincide con
    # el patrón, o `Ninguno` si no coincide.
    
def validarDato(rut):
    patron = r'^\d{1,8}-[\dKk]$'
    return re.match(patron, rut) # retorna un valor booleano


#Esta función valida el rut, ingresando como parámetros el número y el digito verificador

    # '''La función `validarRut` toma una cadena `texto` y una cadena `dvRut` como entrada, y devuelve un
    # valor booleano que indica si el `dvRut` dado es un dígito de verificación válido para el `texto`
    # dado según el algoritmo RUT chileno.
    
    # Parameters
    # ----------
    # texto
    #     El parámetro "texto" representa el número de Rut como una cadena. Es la parte principal del número
    # Rut sin el dígito de verificación.
    # dvRut
    #     El parámetro "dvRut" representa el dígito de verificación esperado del número "RUT" (Rol Único
    # Tributario). El "RUT" es un número de identificación único utilizado en Chile para fines fiscales y
    # legales. El dígito de verificación es el último dígito de la "R
    
    # Returns
    # -------
    #     un valor booleano.
    
    # '''
def validarRut(texto,dvRut):
    suma = pos = 0 
    while -pos < len(texto):
        for i in range (2,8):
            pos -=1
            suma += int(texto[pos]) * i
            if -pos  == len(texto):
                break
        i +=1
    d = 11 - (suma % 11)
    if d == 10:
        dv = "K"
    elif d == 11:
        dv = "0"
    else:
        dv = str(d)
    return dv == dvRut    #Retorna valor booleano


#PROGRAMA VALIDADOR DE RUT CHILENO

#Bloque principal
    # `rut` es una variable que almacena el valor de entrada de la rut (número de identificación
    # chileno) ingresada por el usuario.
    # Este código solicita al usuario que ingrese un número de identificación chileno (RUT) y luego lo
    # valide.
while True:
    rut = input("Ingrese rut: ")
    if validarDato(rut):
        print("verdadero" if validarRut(rut.split('-')[0],rut.split('-')[1].upper()) else "falso")
        break
    else:
        print("Ingrese un numero de rut válido")