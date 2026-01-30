import math
import time
dn = 3 #probando git
ts = 0
movimientos = 0
mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0]]
objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3]]
def dibuja_celda(disco):
    if disco==0:
        print (" "*(dn-disco),"|"," "*(dn-disco), end=""),
    elif disco!=0:
        print (" "*(dn-disco+1),"o"*(2*disco-1)," "*(dn-disco+1), end=""),

def dibujar_torres():
    print ("\n")
    n = 1
    for fila in mundo:
        for columna in fila:
            dibuja_celda(columna)
        print("")
    print ("-"*(dn*8+3))
    print (" "*(dn),"1"," "*(dn*2),"2"," "*(dn*2),"3")

def encuentra_disco_de_arriba(col):
    fila=0
    while fila<=dn and mundo[fila][col]==0:
        fila+=1
    if fila<=dn:
        return mundo[fila][col]
    else:
        return 0

def encuentra_proximo_espacio_en_blanco(col):
    fila=0
    while fila<=dn and mundo[fila][col]==0:
        fila+=1
    return fila-1

def elimina_disco_superior(col):
    fila=0
    while fila<=dn and mundo[fila][col]==0:
        fila+=1
    mundo[fila][col]=0


def Hanoi (discos,TorreOrigen=1,TorreAuxiliar=2,TorreDestino=3):
    global movimientos
    global ts
    if discos==1:
        time.sleep(ts)
        dibujar_torres()
        c0=TorreOrigen- 1
        c1=TorreDestino-1
        disco1=encuentra_disco_de_arriba(c0)
        elimina_disco_superior(c0)
        mundo[encuentra_proximo_espacio_en_blanco(c1)][c1]=disco1
        movimientos+=1
        print("Movimiento", movimientos)
        
    else:
        Hanoi(discos-1,TorreOrigen,TorreDestino,TorreAuxiliar)
        time.sleep(ts)
        dibujar_torres()
        c0=TorreOrigen- 1
        c1=TorreDestino-1
        disco1=encuentra_disco_de_arriba(c0)
        elimina_disco_superior(c0)
        mundo[encuentra_proximo_espacio_en_blanco(c1)][c1]=disco1
        movimientos+=1
        print("Movimiento", movimientos)
        Hanoi (discos-1,TorreAuxiliar,TorreOrigen,TorreDestino)
    return
while True:
    print("===Practica 1===")
    print("Elige una opción")
    print("1-Numero discos")
    print("2-Tiempo entre movimientos")
    print("3-Simular")
    print("4-Salir")
    x= input("Escribe tu elección:")
    y = int(x)
    if(y==1):
        a=int(input("Introduce la cantidad de pruebas\n"))
        dn = a
        if(a==3):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3]]
        elif(a==4):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[4,0,0]]
        elif(a==5):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5]]
        elif(a==6):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],[0,0,6]]
        elif(a==7):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],[0,0,6],[0,0,7]]
        elif(a==8):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[8,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],[0,0,6],[0,0,7],[0,0,8]]
        elif(a==9):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[8,0,0],[9,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],[0,0,6],[0,0,7],[0,0,8],[0,0,9]]
        elif(a==10):
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[8,0,0],[9,0,0],[10,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],[0,0,6],[0,0,7],[0,0,8],[0,0,9],[0,0,10]]
    elif(y==2):
        ts=int(input("Introduce el tiempo entre movimientos\n"))
    elif(y==3):
        Hanoi(dn)
        dibujar_torres()
        print ("Felicitaciones! Ha terminado en",movimientos,"movimientos.")
        print("1-Volver al menu principal")
        print("2-Salir")
        t = int(input("Elije una opccion"))
        if(t==2):
            break
        elif(t==1):
            dn = 3
            ts = 0
            movimientos = 0
            mundo = [[0,0,0],[1,0,0],[2,0,0],[3,0,0]]
            objetivo = [[0,0,0],[0,0,1],[0,0,2],[0,0,3]]
        else:
            print("NUMERO INVALIDO")
    elif(y==4):
        break
    else:
        print("NUMERO INVALIDO")