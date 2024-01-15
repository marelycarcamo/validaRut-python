VALIDADOR DE RUT CHILENO

DESCRIPCION

Este programa en Python está diseñado para validar el Rol Único Tributario (RUT) chileno. El RUT es un número único e irrepetible que se asigna a las personas y empresas en Chile para fines tributarios.

El programa consta de tres partes principales:

Función validarDato(dato): Esta función toma un RUT como entrada y verifica si el formato del RUT es válido. El formato correcto es un número de 1 a 8 dígitos seguido de un guión y luego un dígito verificador, que puede ser un número o las letras ‘K’ o ‘k’.


Función validarRut(texto, dvRut): Esta función toma un número de RUT y un dígito verificador como entrada. Calcula el dígito verificador del número de RUT utilizando el algoritmo estándar y luego compara el resultado con el dígito verificador proporcionado. Si coinciden, la función devuelve True; de lo contrario, devuelve False.


Bucle principal: Este es un bucle while que solicita al usuario que ingrese un RUT. Si el RUT es válido, el programa verifica el dígito verificador y luego imprime si el RUT es válido o no. Si el RUT no es válido, el programa solicita al usuario que ingrese un nuevo RUT.

Para usar este programa, simplemente ejecútalo y sigue las instrucciones en pantalla para ingresar un RUT. El programa te dirá si el RUT es válido o no.
