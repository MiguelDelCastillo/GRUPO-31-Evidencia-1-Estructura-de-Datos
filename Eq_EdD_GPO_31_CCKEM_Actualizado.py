from datetime import datetime
from collections import namedtuple

Datos = namedtuple("Ventas",("descripcion", "cantidad_pzas","precio_venta", "fecha"))
lista_ventas = []
diccionario_ventas = {}

while True:
    
    print("\tLlantas Michelin")
    print("")
    print("1) Registrar una venta")
    print("2) Busqueda especifica de una venta")
    print("3) Salir")
    print("\nUtilize los numeros: 1, 2, y 3")
    respuesta = int(input("Elija una opción: "))
    
    if respuesta == 1:
        lista_ventas = []
        while True:
            folio = int(input('\nIngrese la clave del usuario: '))
            if folio in diccionario_ventas.keys():
                print('Esta clave ya existe, porfavor ingresa otra')
            else:
                break
        while True:
            descripcion = input('Ingrese la descripcion de la llanta: ')
            cantidad_pzas = input('Ingrese la cantidad de piezas a comprar: ')
            precio_venta = input('Ingrese el precio unitario de cada pieza: ')
            print("---------------------------------")
            
            # Lista
            now = datetime.now()
            fecha_venta = now.strftime("%m/%d/%Y, %H:%M:%S")
            ventas = Datos(descripcion,cantidad_pzas, precio_venta, fecha_venta)
            lista_ventas.append(ventas)
            
            # Diccionario
            diccionario_ventas[folio] = lista_ventas
            respuesta1 = int(input('¿Quieres seguir agregando productos?\n\t 1: Si\n\t 2: No\n\t'))
            if (respuesta1 != 1):
                tamañoLista = 0
                total_ventas = 0
                while tamañoLista < len(diccionario_ventas[folio]):
                    total_ventas = (int(diccionario_ventas[folio][tamañoLista].precio_venta) * int(diccionario_ventas[folio][tamañoLista].cantidad_pzas)) + total_ventas
                    tamañoLista = tamañoLista + 1
                print(f"Total de las ventas: {total_ventas}")
                print(f"El iva aplicable es de: {total_ventas * .16}")
                print(f"El total con iva aplicado es de: {round(total_ventas*1.16, 2)}")
                break
                
    elif respuesta == 2:
        
        busqueda = int(input("Ingresa la clave a buscar: "))
        tamañoLista = 0
        total_ventas = 0
        if busqueda in diccionario_ventas.keys():
            while tamañoLista < len(diccionario_ventas[busqueda]):
                print("\n**********************************************")
                print(f"Descripcion de la Llanta: {diccionario_ventas[busqueda][tamañoLista].descripcion}")
                print(f"Cantidad de Piezas: {diccionario_ventas[busqueda][tamañoLista].cantidad_pzas}")
                print(f"Precio de Venta: {diccionario_ventas[busqueda][tamañoLista].precio_venta}")
                print(f"Fecha de la Venta: {diccionario_ventas[busqueda][tamañoLista].fecha}")
                print("**********************************************\n")
                total_ventas = (int(diccionario_ventas[busqueda][tamañoLista].precio_venta) * int(diccionario_ventas[busqueda][tamañoLista].cantidad_pzas)) + total_ventas
                tamañoLista = tamañoLista + 1
            print(f"Total de las ventas: {total_ventas}")
        else:
            print("La clave no esta registrada")
                            
    elif respuesta == 3:
        print("Finalizando")
        break