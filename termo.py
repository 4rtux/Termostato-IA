
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bellman_ford(on_cost, off_cost):
    # Importar matrices de transicion de ON y OFF
    on_matrix = pd.read_csv('ON.csv', delimiter=',', index_col=0)
    off_matrix = pd.read_csv('OFF.csv', delimiter=',', index_col=0)

    # Las filas ya tienen indices del 0 al 18 pero las columnas tienen las temperaturas como indices
    # Trasponer las matrices, poner indices de 0 a 18 y volver a trasponer para que las columnas tengan indices del 0 al 18
    on_matrix = on_matrix.T.reset_index(drop=True).T
    off_matrix = off_matrix.T.reset_index(drop=True).T

    print('ON matrix:\n', on_matrix)
    print('OFF matrix:\n ', off_matrix)
    
    # Inicializar las listas de V_actual , V_anterior y la politica que guardaran los valores de V y la politica optima para cada estado
    num_states = len(on_matrix)
    policy = [0] * num_states
    V_previous = [0] * num_states
    V_current = [0] * num_states
    # converges indicará si V_current y V_previous son iguales, es decir, si se ha alcanzado la convergencia
    converges = False
    # Calcular V para cada estado usando la ecuacion de Bellman
    while not converges:
        for state in range(num_states):
            V_on = on_cost + sum([on_matrix[state][next_state] * V_previous[next_state] for next_state in range(num_states)])
            V_off = off_cost + sum([off_matrix[state][next_state] * V_previous[next_state] for next_state in range(num_states)])
            # Uso el round para redondear a 3 decimales, que agiliza el proceso y no supone grandes problemas de precision
            V_current[state] = min(round(V_on,3),round(V_off,3))
            # Elegir la accion que minimiza el coste
            print(V_current)
            if V_on < V_off:
                policy[state] = 1
            else:
                policy[state] = 0
        # Comprobar si se ha alcanzado la convergencia
        if V_current == V_previous:
            converges = True
        # Si no se ha alcanzado la convergencia, actualizar V_previous para la siguiente iteracion
        else:
            V_previous = list(V_current)
    print("sale del bucle")
    # Calcular V para cada estado usando la ecuacion de Bellman
    # Empezando desde un estado aleatorio, seguir la politica optima hasta alcanzar la convergencia a 22 grados
    state = np.random.randint(0, num_states)
    print(state)
    # Crear lista de temperaturas para poder saber a que temperatura corresponde cada estado
    # Los estados tienen indices del 0 al 18, pero las temperaturas van de 16 a 25.5 de 0.5 en 0.5
    # Esto se hace para que la representacion grafica sea mas intuitiva y contenga las temperaturas reales en lugar de los indices
    temperatures = []
    for i in np.arange(16, 25.5, 0.5):
        temperatures.append(i)
    # Lista que guarda el recorrido de temperaturas que sigue el sistema
    route = []
    route_with_itertions = []
    route_with_itertions.append(temperatures[state])
    route.append(temperatures[state])

    if state == 12:
        expected_state = True
    expected_state = False
    n_it = 300
    iterations = 0
    
    # Seguir la politica optima hasta alcanzar la temperatura objetivo
    for i in range(n_it):
        # Si la politica es 1 para el estado state, se usan las probabilidades de la matriz ON para calcular el siguiente estado
        if policy[state] == 1:
            state = np.random.choice(range(num_states), p=on_matrix.iloc[state])
            # p es la probabilidad de que ocurra cada uno de los estados, por eso, a pesar de que ponga random.choice, no es random
        # Si la politica es 0 para el estado state, se usan las probabilidades de la matriz OFF para calcular el siguiente estado
        else:
            state = np.random.choice(range(num_states), p=off_matrix.iloc[state])
        # Guardar la temperatura correspondiente al estado en la lista route
        if expected_state == False:
            iterations += 1
            route.append(temperatures[state])
        route_with_itertions.append(temperatures[state])
        if state == 12:
            # Se alcanzan los 22 grados
            expected_state = True

    # Muestra la ruta con 300 iteraciones ignorando que el estado 12 es absorbente
    plt.title('300 iterations without absorbing state')
    plt.xlabel('Iterations')
    plt.ylabel('Temperatures')
    plt.plot(route_with_itertions)
    print('Route with 300 iterations printed')
    plt.show()

    if expected_state == True:    
        # Muestra las iteraciones que se han necesitado para alcanzar la temperatura objetivo
        plt.title('Iterations needed to reach 22 degrees')
        plt.xlabel('Iterations')
        plt.ylabel('Temperatures')
        plt.plot(route)
        print('Normal route printed')
        plt.show()
        print('22 degrees reached with', iterations, 'iterations!')

    else:
        # Si con 300 iteraciones no se alcanza la temperatura objetivo, se muestra un mensaje de error
        print('22 degrees not reached with 300 iterations')

    return policy

# Ejemplo de uso
# Coste optimo es 3 en ON y 4 en OFF
costo_on = 1
costo_off = 4

valores_V = bellman_ford(costo_on, costo_off)
print(valores_V)
