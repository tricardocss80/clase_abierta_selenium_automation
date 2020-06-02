ford = 100000
chevrolet = 120000
fiat = 80000

p2 = 50000
p4 = 65000
p5 = 78000

blanco = 10000
azul = 20000
negro = 30000

hay_cliente = 'si'
contador = 0

venta = []

def marca_input():
    marca = ""
    while marca != "ford" and marca != "chevrolet" and marca != "fiat":
        marca = input("Ingrese por favor la marca de su nuevo auto: ")
        if marca != "ford" and marca != "chevrole" and marca != "fiat":
            print("Debe elegir una marca disponible")
    return marca


def puertas_input():
    puertas = ""
    while puertas != '2' and puertas != '4' and puertas != '5':
        puertas = input("Ingrese por favor la cantidad de puertas de su nuevo auto: ")
        if puertas != '2' and puertas != '4' and puertas != '5':
            print("Debe elegir la cantidad de puertas disponible")
    return puertas


def color_input():
    color = ""
    while color != 'blanco' and color != 'azul' and color != 'negro':
        color = input("Ingrese por favor el color de su nuevo auto: ")
        if color != 'blanco' and color != 'azul' and color != 'negro':
            print("Debe elegir un color disponible")
    return color


def precio_marcas(marca):
    if marca == "ford":
        return ford
    elif marca == "chevrolet":
        return chevrolet
    elif marca == "fiat":
        return fiat


def precio_puertas(puertas):
    if puertas == '2':
        return p2
    elif puertas == '4':
        return p4
    elif puertas == '5':
        return p5


def precio_color(color):
    if color == "blanco":
        return blanco
    elif color == "azul":
        return azul
    elif color == "negro":
        return negro


def precio_inicial(marca,puertas,color):
    return precio_marcas(marca) + precio_puertas(puertas) + precio_color(color)


def descuento(contador,valor):
    if contador > 5 and contador < 11:
        return valor * 0.9
    elif contador > 10 and contador < 51:
        return valor * 0.85
    elif contador > 50:
        return valor * 0.82
    else:
        return valor


while hay_cliente == 'si':
    contador = contador + 1
    print('Cliente Nº: ' + str(contador))

    nombre = input("Ingrese por favor su nombre: ")
    apellido = input("Ingrese por favor su apellido: ")
    marca = marca_input()
    puertas = puertas_input()
    color = color_input()
    precio = precio_inicial(marca,puertas,color)

    items = {'cliente': contador, 'nombre': nombre, 'apellido': apellido, 'marca': marca, 'puertas': puertas,
              'color': color, 'precio': precio}

    venta.append(items)

    hay_cliente = input('¿Hay mas clientes?: ')
    if hay_cliente == 'no':
        cantidad = len(venta)
        for i in venta:
            precio = descuento(cantidad, i['precio'])
            print("La persona: " + i['nombre'] + " " + i['apellido'] + " ""compro un auto " + i['marca'] + " de "
                  + str(i['puertas']) + " puertas y color " + i['color'] + " con un precio de $" + str(precio))