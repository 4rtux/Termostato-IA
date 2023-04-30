import math
import pandas as pd
import numpy as np


ON = pd.read_csv('ON.csv', delimiter=',', index_col=0)
OFF = pd.read_csv('OFF.csv', delimiter=',', index_col=0)
ON = ON.T.reset_index(drop=True).T # Sirve para que los índices de las columnas sean enteros de 0 a n
OFF = OFF.T.reset_index(drop=True).T

print(ON)
print(OFF)
print("\n")



def bellman(costeON: int, costeOFF: int) -> list:
    Vant = []
    Vactual = []
    for estado in range(len(ON)):
        Vant.append(0)
        Vactual.append(0)
    conv = False
    while conv == False:
        Vant = Vactual
        for i in range(len(ON)):
            sum1 = costeON
            sum2 = costeOFF
            for j in range(len(ON)):
                sum1 += ON[j][i]*Vant[j]
                sum2 += OFF[j][i]*Vant[j]
            Vactual[i] = min(sum1, sum2)
        print(Vactual)
        if Vactual[i] == Vant[i]:
                conv = True

    print(Vactual)
    return Vactual

def bellman_ford(on_cost, off_cost):
    # Import transition probability matrices for ON and OFF states
    on_matrix = pd.read_csv('ON.csv', delimiter=',', index_col=0)
    off_matrix = pd.read_csv('OFF.csv', delimiter=',', index_col=0)
    on_matrix= on_matrix.T.reset_index(drop=True).T # Sirve para que los índices de las columnas sean enteros de 0 a n
    off_matrix = off_matrix.T.reset_index(drop=True).T
    
    # Initialize V_previous and V_current lists
    num_states = len(on_matrix)
    policy = [0] * num_states
    V_previous = [0] * num_states
    V_current = [0] * num_states
    
    # Calculate V for each state using Bellman equation
    while True:
        for state in range(num_states):
            V_on = on_cost + sum([on_matrix[state][next_state] * V_previous[next_state] for next_state in range(num_states)])
            V_off = off_cost + sum([off_matrix[state][next_state] * V_previous[next_state] for next_state in range(num_states)])
            if V_on < V_off:
                policy[state] = 1
            else:
                policy[state] = 0
            V_current[state] = min(V_on, V_off)
        print('V_previous:', V_previous, '\n')
        print('V_current:', V_current, '\n')
        print('-----------------------------------\n')
        if V_current == V_previous:
            break
        else:
            V_previous = list(V_current)
    
    return V_current, policy

    """def policy(V, on_cost, off_cost):
    # Import transition probability matrices for ON and OFF states
    on_matrix = pd.read_csv('ON.csv', delimiter=',', index_col=0)
    off_matrix = pd.read_csv('OFF.csv', delimiter=',', index_col=0)
    on_matrix= on_matrix.T.reset_index(drop=True).T # Sirve para que los índices de las columnas sean enteros de 0 a n
    off_matrix = off_matrix.T.reset_index(drop=True).T

    # Initialize policy list
    policy = [0] * len(V)

    # Calculate policy for each state
    for state in range(len(V)):
        V_on = on_cost + sum([on_matrix[state][next_state] * V[next_state] for next_state in range(len(V))])
        V_off = off_cost + sum([off_matrix[state][next_state] * V[next_state] for next_state in range(len(V))])
        if V_on < V_off:
            policy[state] = 1
        else:
            policy[state] = 0

    return policy

    """

    """
    #IMPLEMENTACIÓN 1 DE CHATGPT
    matriz_ON = pd.read_csv('ON.csv', index_col=0)
    matriz_OFF = pd.read_csv('OFF.csv', index_col=0)

    # Inicializar listas V_anterior y V_actual
    n = len(matriz_ON)
    V_anterior = pd.Series([0] * n, index=matriz_ON.index)
    V_actual = pd.Series([0] * n, index=matriz_ON.index)

    # Calcular valor de V para cada estado mediante la ecuación de Bellman
    for k in range(100): # número máximo de iteraciones
        for i in matriz_ON.index:
            sum_ON = 0
            sum_OFF = 0
            for j in matriz_ON.index:
                sum_ON += matriz_ON.loc[i, j] * (costeON + V_anterior[j])
                sum_OFF += matriz_OFF.loc[i, j] * (costeOFF + V_anterior[j])
            V_actual[i] = min(sum_ON, sum_OFF)
        if V_actual.equals(V_anterior): # si las listas son iguales, terminar las iteraciones
            break
        else:
            V_anterior = V_actual.copy()

    # Retornar lista V_actual
    return V_actual"""

    """#IMPLEMENTACIÓN 2 DE CHATGPT
    V_anterior = [0 for i in range(len(ON))]
    V_actual = [0 for i in range(len(ON))]

    while True:
        # Actualizar los valores de V
        for estado in range(len(ON)):
            valores_posibles = []
            for i in range(len(ON)):
                valor_posible = ON[i][estado] * (costeON + V_anterior[i]) + \
                                OFF[i][estado] * (costeOFF + V_anterior[i])
                valores_posibles.append(valor_posible)
            V_actual[estado] = max(valores_posibles)

        # Comprobar si los valores de V han convergido
        if np.allclose(V_actual, V_anterior, rtol=1e-06, atol=1e-06):
            return V_actual

        # Actualizar V_anterior
        V_anterior = V_actual.copy()
        V_actual = [0 for i in range(len(ON))]

    """

    """while conv == False:
        if len(Vactual) != 0:
            Vant = Vactual
        print("Vanterior:", Vant ,"\n")
        print("Vactual:", Vactual, "\n")
        Vactual = []
        for i in range(len(ON)):
            for j in range(len(ON)):
                sum1 += ON[j][i]*Vant[j]
                sum2 += OFF[j][i]*Vant[j]
            Vactual.append(min(sum1, sum2))
        print("Vactual cambiada:",Vactual, "\n")
        print("sum1:", sum1, "\n")
        print("sum2:", sum2, "\n")
        print("-----------------------------------\n")
        for i in range(len(ON)):
            if Vactual[i] == Vant[i]:
                conv = True"""
    
    """
    conv = False
    while conv == False:
        if len(Vactual) != 0:
            Vant = Vactual
        print("Vanterior:", Vant ,"\n")
        print("Vactual:", Vactual, "\n")
        Vactual = []
        for i in range(len(ON)):
            row_list_ON = ON.iloc[[i]].values.flatten().tolist()
            row_list_OFF = OFF.iloc[[i]].values.flatten().tolist()
            for j in range(len(ON)):
                sum1 += row_list_ON[j]*Vant[j]
                sum2 += row_list_OFF[j]*Vant[j]
            Vactual.append(round(min(sum1, sum2),1))
        print("Vactual cambiada:",Vactual, "\n")
        print("sum1:", sum1, "\n")
        print("sum2:", sum2, "\n")
        print("-----------------------------------\n")
        for i in range(len(ON)):
            if Vactual[i] == Vant[i]:
                conv = True
    """


    """for i in range(len(ON)):
        row_list_ON = ON.iloc[[i]].values.flatten().tolist()
        row_list_OFF = OFF.iloc[[i]].values.flatten().tolist()
        print(row_list_ON)
        for j in range(len(ON)):
            sum1 += row_list_ON[j]*Vant[j]
            sum2 += row_list_OFF[j]*Vant[j]
        V.append(round(min(sum1, sum2)),2)
    for i in range(len(ON)):
        Vant[i] = V[i]"""
    

    return Vactual








    print(Vant)
    for i in Vnuevo:
        V.append(i)
    """for estado in range(len(ON)):
        Vnuevo[estado] += ON[estado][estado] * costeON
        V.append(Vnuevo[estado])"""

    """for estado in range(len(ON)):
        for estado2 in range(len(ON)):
            Vant[estado] += ON[estado][estado2] * costeON[estado2]
            Vant[estado] += OFF[estado][estado2] * costeOFF[estado2]
        V.append(Vant[estado])"""
    return V

# Ejemplo de uso

costo_on = 1
costo_off = 1

valores_V = bellman_ford(costo_on, costo_off)
print(valores_V)