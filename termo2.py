"""Clase termo"""
"""Se quiere construir un termostato que optimice el consumo de energía, pero buscando el confort del usuario. El funcionamiento básico en este caso será:
1. El usuario indica en el termostato la temperatura a la que le gustaría que se encuentre una estancia. Para esta práctica, supondremos que la temperatura que desea el usuario es 22 grados centígrados.
2. El termostato incorpora un termómetro que mide la temperatura real de la estancia, dando un valor que puede estar entre 16 y 25 grados, de medio grado en medio grado.
3. Por simplicidad, consideramos que no pueden producirse temperaturas ni inferiores ni superiores a las dadas [R1].
4. El termostato debe decidir, en intervalos de media hora, si encender o apagar la calefacción. Por ejemplo, a las 15:00 decide encenderla, a las 15:30 nuevamente encenderla y a las 16:00 apagarla. En este caso, la calefacción estaría encendida desde las 15:00 hasta las 16:00 y apagada desde las 16:00 hasta las 16:30.
Con la calefacción encendida, al transcurso de media hora, la temperatura de la estancia habrá subido medio grado la mitad de las veces. El 20% de las veces habrá subido un grado, el 20% se habrá quedado igual y el 10% de las veces incluso habrá bajado medio grado. Excepciones:
• Si la temperatura es 16º, como ya no puede bajar más por [R1], el 30% de las veces se queda igual. Sube uno o medio grado en el mismo porcentaje que para el resto de temperaturas.
• Si es 25, no puede subir. El 10% de las veces baja y el resto se queda igual.
• Si es 24.5, solo puede subir medio grado, lo que sucede el 70% de las veces. El 20% de las veces se queda igual.
Con la calefacción apagada, el cambio de temperatura en media hora habrá sido de -0.5 grados el 70% de las veces, de +0.5 grados el 10% de las veces y no habrá cambios el resto. Excepciones:
• Si la temperatura es 16º, como ya no puede bajar más por [R1], el 90% de las veces se queda igual.
• Si es 25, no puede subir. El 30% de las veces se queda igual

El termostato se basará en la política óptima del PDM correspondiente a este problema, con el objetivo de que la temperatura real coincida con la marcada por el usuario, en cuyo momento el termostato deja de funcionar. 

Datos de ayuda para el desarrollo en Python:
Con esto podemos asumir que hay 19 estados que representan cada una de las temperaturas posibles. 
Las funciones de transición son apagar o encender. 
Hay que usar cadenas de Markov y programar el algoritmo de Bellman para el desarrollo.
Hacer un análisis de costes.
Calcular valores v de cada uno de los estados.
Calcular camino mínimo desde cualquier estado.
Se proporcionan los archivos ON.csv y OFF.csv con las probabilidades de transición de cada estado 
a cada estado, en función de si se enciende o se apaga la calefacción.
"""
import pandas as pd
import numpy as np
df1 = pd.read_csv('ON.csv', sep=',', engine='python')
df2 = pd.read_csv('OFF.csv', sep=',', engine='python')















"""
import numpy as np

# Cargar la matriz de probabilidades de transición desde un archivo csv
P_on = np.genfromtxt('probabilidades_on.csv', delimiter=',')
P_off = np.genfromtxt('probabilidades_off.csv', delimiter=',')
P = np.zeros((19, 19))
for i in range(19):
    for j in range(19):
        P[i][j] = P_on[i][j] + P_off[i][j]

# Crear la matriz de adyacencia
n = len(P)
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if P[i][j] > 0:
            A[i][j] = -np.log(P[i][j])

# Crear la matriz de costes
C = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if P[i][j] > 0:
            C[i][j] = 1

# Crear la matriz de costes acumulados
C_acum = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if P[i][j] > 0:
            C_acum[i][j] = 1 + C_acum[i][j-1]

"""



      





