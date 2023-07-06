import numpy as np
from Asistente import *

arreglo = np.full((10,10),'---')
lista_Asistente = []
def Llenar(arreglo):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            arreglo[f][c] = str(x)

def Mostrar(arreglo):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + ' | ' + arreglo[f][c]
        print(fila)

def ComprarAsiento(arreglo, num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                arreglo[f][c] = 'X'

def ComprobarAsiento(arreglo, num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                if arreglo[f][c] == 'X':
                    return False
    return True

def AgregarAsistente(lista_Asistente, num_asiento):
    a = Asistente()
    a.rut = int(input("ingrese su rut (sin guion ni DV):  "))
    a.nombre = input("ingrese su nombre:    ")
    a.apellido = input("ingrese su apellido:    ")
    a.num_asiento = num_asiento
    if num_asiento >= 1 and num_asiento <= 20:
        a.valor = 120000
    if num_asiento >= 21 and num_asiento <= 50:
        a.valor = 80000
    if num_asiento >= 51 and num_asiento <= 120:
        a.valor = 50000
    a.valor_entrada = a.valor
    print("asistente agregado correctamente")
    lista_Asistente.append(a)

def ComprarEntrada (arreglo,lista_Asistente):
    try:
        cantidad = int(input("selecccione cantidad de entradas (entre 1 y 3):   "))
        if cantidad >= 1 and cantidad <= 3:
            Compra = 0
            while Compra < cantidad:
                Mostrar(arreglo)
                num_asiento = int(input("seleccione el numero de asiento que desea (entre 1 y 100): "))
                if num_asiento >=1 and num_asiento <= 100:
                    disponible = ComprobarAsiento(arreglo, num_asiento)
                    if disponible == True:
                        AgregarAsistente(lista_Asistente, num_asiento)
                        ComprarAsiento(arreglo, num_asiento)
                        Compra = Compra + 1
                    else:
                        print("NO se encuentra disponible, elija otra opcion")
                else:
                    print("asientos disponibles entre 1 y 100, seleccione otra opcion")
        else:
            print("Exede maximo de entradas por compra (maximo 3 entradas por compra")
    except BaseException as error:
        print(f"error: {error}")

def ListadoAsistentes(lista_asistente):
    for asistente in lista_asistente:
        print(f"nombre : {asistente.nombre}")
        print(f"apellido : {asistente.apellido}")
        print(f"rut : {asistente.rut}")
        print(f"numero de asiento : {asistente.num_asiento}")
        print(f"valor entrada : {asistente.valor_entrada}")
def Totales (Lista_Asistente):
    platinum = 0
    gold = 0
    silver = 0
    t_platinum = 0
    t_gold = 0
    t_silver = 0
    for a  in lista_Asistente:
        if a.valor == 120000:
            platinum += 1
            t_platinum += 120000
        if a.valor == 80000:
            gold += 1
            t_gold += 80000
        if a.valor == 50000:
            silver += 1
            t_silver += 50000
    print(f" entradas platinum: {platinum}, total facturado: ${t_platinum}")
    print(f" entradas gold: {gold}, total facturado: ${t_gold}")
    print(f" entradas silver: {silver}, total facturado: ${t_silver}")
    tot_total = t_platinum + t_gold + t_silver
    tot_entradas = platinum + gold + silver
    print(f" total cantidad de entradas: {tot_entradas}")
    print(f" total facturado: {tot_total}")

def Salir ():
    print("gracias por comprar sus entradas")
    print("¡¡¡creativos.cl te desea lo mejor en tu concierto!!!")
    print("Lucas Venditti 002D")
    print("06-07-2023")
    return False