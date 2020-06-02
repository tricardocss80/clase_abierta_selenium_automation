
#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#*Nombre y apellido del comprador. / *Marca / *Puertas / *Color
# Marcas posibles y sus precios: -Ford $100000 / -Chevrolet: $120000 / -Fiat: $80000
# -Por la cantidad de puertas se añade un precio: -2: $50000 / -4: $65000 / -5: $78000
#Dependiendo del color, se deben sumar: -Blanco: $10000 / -Azul: $20000 / -Negro: $30000
# Deben imprimirse los datos de cada compra y el precio total.


programa = False
i = 1

Ford = 100000
Chevrolet = 120000
Fiat = 80000

p2 = 50000
p4 = 65000
p5 = 78000

blanco = 10000
azul = 20000
negro = 30000



while programa == False:
    if i == 5:
        programa = True
    print("Cliente Nº" + str(i))
    i = i + 1



    def marca_input():
        marca = ""
        while marca != "Ford" and marca != "Chevrolet" and marca != "Fiat":
            marca = input("Ingrese por favor la marca de su nuevo auto: ")
            if marca != "Ford" and marca != "Chevrole" and marca != "Fiat":
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





    def datos_del_comprador(nombre,apellido,marca,puertas,color,precio):
        print("El señor " +nombre + " " +apellido+" eligio el auto "+marca+" con "+puertas + " puertas, de color "+color+ " y su precio es "+str(precio))

    def precio_marcas(marca):
        if marca == "Ford":
            return Ford
        elif marca == "Chevrolet":
            return Chevrolet
        elif marca == "Fiat":
            return Fiat



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


    nombre = input("Ingrese por favor su nombre: ")
    apellido = input("Ingrese por favor su apellido: ")
    marca = marca_input()
    puertas = puertas_input()
    color = color_input()
    precio = precio_marcas(marca) + precio_puertas(puertas) + precio_color(color)
    datos_del_comprador(nombre, apellido, marca, puertas, color, precio)

