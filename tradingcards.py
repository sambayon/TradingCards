import random 
import statistics

def crear_album(figus_total):
    album = []
    i = 0
    while i < figus_total:
        album = album + [0]
        i = i + 1
    return album

"""Suppose we buy individual single trading cards"""
def hay_alguno(lista, elem):
    i = 0
    hay_alguno = False
    while i < len(lista):
        if lista[i] == elem:
            hay_alguno = True
        i += 1
    return hay_alguno


def comprar_una_figu(figus_total):
    return random.randint(1, figus_total)

def cuantas_figus(figus_total):
    contador = 0
    album = crear_album(figus_total)
    i = 0
    while 0 in album:
        figu = comprar_una_figu(figus_total)
        if hay_alguno(album, figu) == False:
            album[figu - 1] = 1
            contador += 1
        else:
            contador += 1
    return contador 

def experimento(figus_total, n_rep):
    explist = []
    for i in range(0, n_rep):
        t = cuantas_figus(figus_total)
        explist.append(t)
    return explist
    

"""What if we had a pack containing 5 trading cards
and 670 unique cards to complete the album?"""

def generar_paquete(figus_total, figus_paquete):
    i = 0
    paquetes = []
    while i < figus_paquete:
        paquetes.append(random.randint(0, figus_total -1))
        i += 1
    return paquetes

def cuantos_paquetes(figus_total, figus_paquete):
    paquetes = 0
    album = crear_album(figus_total)
    while 0 in album:
        paquetes += 1
        paquete = generar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i - 1] = 1
    return paquetes

def experimento2(figus_total, figus_paquete, n_rep):
    explist = []
    for i in range(0, n_rep, 1):
        explist.append(cuantos_paquetes(figus_total, figus_paquete))
    return explist

case = experimento2(670, 5, 100)
print("100 albums completition:")
print(case)
print("Mean value:")
print(statistics.mean(case))
print("Median:")
print(statistics.median(case))
print("Std:")
print(statistics.stdev(case))