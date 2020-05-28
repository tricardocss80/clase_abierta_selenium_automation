# Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
# Se pide imprimir el nombre, el apellido y el promedio.
# Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4
# puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
# En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".


print("Bienvenido al sistema de calificaciones de la escuela")


def promedio_materias(matematica, literatura, fisica):
    return (matematica + literatura + fisica) / 3


nombre = input("Ingresa tu nombre por favor: ")
apellido = input("Ingresa tu apellido por favor: ")
print("Es un gusto saludarte " + nombre, apellido)


matematica = float(input("Ingresa por favor tu nota de Matematica: "))
if matematica > 0 and matematica < 11:
    print("Ingresaste: " + str(matematica))
else:
    print("Debes ingresar un numero entre 1 y 10")


literatura = float(input("Ingresa por favor tu nota de Literatura: "))
if literatura > 0 and literatura < 11:
    print("Ingresaste: " + str(matematica))
else:
    print("Debes ingresar un numero entre 1 y 10")

fisica = float(input("Ingresa por favor tu nota de Fisica: "))
if fisica >0 and fisica < 11:
    print("Ingresaste: " + str(fisica))
else:
    print("Debes ingresar un numero entre 1 y 10")

promedio = promedio_materias(matematica, literatura, fisica)

print("Tu promedio es: " + str(promedio))

if promedio >= 6:
    print("Aprobado")
    if promedio >= 9:
        print("Alumno destacado")

elif promedio >= 4 and promedio <= 5.99999:
    print("A recuperatorio")

else:
    print("Insuficiente")

print("Gracias por utilizar el sistema de calificaciones de la escuela")
