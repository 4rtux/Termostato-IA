import numpy as np

# Cargar la matriz de probabilidades de transición desde un archivo csv
P = np.genfromtxt('probabilidades.csv', delimiter=',')

# Crear la matriz de adyacencia
n = len(P)
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if P[i][j] > 0:
            A[i][j] = -np.log(P[i][j])

# Función para calcular el camino mínimo utilizando el algoritmo de Bellman-Ford
def bellman_ford(A, s):
    n = len(A)
    d = np.full(n, np.inf)
    d[s] = 0
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if A[u][v] != 0:
                    if d[u] + A[u][v] < d[v]:
                        d[v] = d[u] + A[u][v]
    return d

# Calcular el camino mínimo desde cualquier estado
for s in range(n):
    d = bellman_ford(A, s)
    print('Desde el estado', s, 'el camino mínimo es:', d)

"""class Termostato:
    def __init__(self, P_on_file, P_off_file):
        self.P_on = np.genfromtxt(P_on_file, delimiter=',')
        self.P_off = np.genfromtxt(P_off_file, delimiter=',')

    def calcular_camino_minimo(self):
        n = len(self.P_on)
        A_on = np.zeros((n, n))
        A_off = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if self.P_on[i][j] > 0:
                    A_on[i][j] = -np.log(self.P_on[i][j])
                if self.P_off[i][j] > 0:
                    A_off[i][j] = -np.log(self.P_off[i][j])"""
