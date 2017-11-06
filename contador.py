import math
from time import time
contador=0
tiempoInicial=time()
while contador < 1000000:
    contador = contador + 1
    print(contador)
tiempoFinal=time()
tiempoEjecucion=tiempoFinal-tiempoInicial
print("Tiempo de ejecucion: "+str(tiempoEjecucion)+" segundos")