import numpy as np
from Asistente import *
from Funciones import *

ciclo = True

Llenar(arreglo)

while ciclo:
    print(" bienvenido VENTA DE ENTRADAS creativos.cl ")
    print("1)   comprar entradas")
    print("2)   mostrar ubicaciones disponibles")
    print("3)   ver listado asistentes")
    print("4)    mostrar ganacias totales")
    print("5)    salir")
    try:
        op = int(input("seleccione 1 opcion (entre 1 y 5):  "))
        match op:
            case 1:
                ComprarEntrada(arreglo, lista_Asistente)
            case 2:
                Mostrar(arreglo)
            case 3:
                ListadoAsistentes(lista_Asistente)
            case 4:
                Totales(lista_Asistente)
            case 5:
                Salir()
            case _:
                print("opcion seleccionada incorrecta")
    except BaseException as error:
        print(f"error: {error}")

