import numpy
import random

def generarMatriz(N,numCel):
    mat=numpy.zeros([N,N])
    for i in range(0,numCel):
        flag=1
        while(flag==1):
            indX=random.randint(0,N-1)
            indY=random.randint(0,N-1)
            if mat[indX,indY]==0:
                mat[indX,indY]=1
                flag=0
    return mat

#evalua si en la posicion X e Y, de la matriz M1 el estado,
# valor 0: esta muerto
# valor 1: esta vivo
# valor 2: esta fuera de rango
def estaVivo(M1, posicionX, posicionY):
    largo = M1.shape
    try:
        if posicionY < 0 or posicionX < 0:
            return 2.0
        elif largo[1] <= posicionY or largo[0] <= posicionX:
            return 2.0
        else:
            return M1[posicionX][posicionY]
    except:
        return 2.0 #fuera de la region

def buscarVida(M1, posicionX, posicionY ):
    buscador = []
    valores = 0
    #posicion de arriba
    buscador.append(estaVivo(M1, posicionX-1, posicionY-1))
    buscador.append(estaVivo(M1, posicionX, posicionY-1))
    buscador.append(estaVivo(M1, posicionX+1, posicionY-1))

    #posiciones horizontales adycentes
    buscador.append(estaVivo(M1, posicionX-1, posicionY))
    buscador.append(estaVivo(M1, posicionX+1, posicionY))

    #posicion en la linea de abajo
    buscador.append(estaVivo(M1, posicionX-1, posicionY+1))
    buscador.append(estaVivo(M1, posicionX, posicionY+1))
    buscador.append(estaVivo(M1, posicionX+1, posicionY+1))

    #suma las posiciones con valores vivos, osea 1
    for valor in buscador:
        if valor == 1.0:
            valores = valores + 1

    #logica,
    # celula viva, con 2 o 3 se mantiene viva
    # celula muerta, con 3 celulas vivas adyacentes vive
    if M1[posicionX][posicionY] == 1 and (2 == valores or valores == 3):
        valores = 1
    elif M1[posicionX][posicionY] == 0 and valores == 3:
        valores = 1
    else:
        valores = 0
    return valores

#se ejecuta un ciclo del juego de la vida
def juegoVidaEjecucion(mat):
    #se hace una copia de la matriz, para guardar los resultados
    matAux = mat.copy()
    #recorre la matriz y en el valor value se obtiene el valor
    for (x,y), valor in numpy.ndenumerate(mat):
        matAux[x][y] = buscarVida(mat, x, y)
    return matAux

#se ejecuta el ciclo de la vida ... por 1000 ciclos
def juegoVida(mat):
    matAux = mat.copy()
    for i in range(1000):
        matAux = juegoVidaEjecucion(matAux).copy()
    return matAux

# ingreso del tamano de la matriz
N = 5
#ingreso de la cantidad de celulas
numCel = 9
M1=generarMatriz(N,numCel)
print(M1.astype(int))
print("")
M2=juegoVida(M1)
print(M2.astype(int))
