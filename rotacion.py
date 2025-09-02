import numpy as np

def rot_x(vector, angulo):
    ''''
        Dado un vector y los grados, devuelve el vector rotado en el eje X esa cantidad de grados
    Parameters:
        vector (np.array): vector que se desea rotar en eje X.
        angulo (float):    grados a rotar el vector.

    Returns:
        np.array: vector girado en el eje x
    '''
    angulo = np.deg2rad(angulo)
    matriz = np.array([[1, 0, 0], [0, np.cos(angulo), -np.sin(angulo)], [0, np.sin(angulo), np.cos(angulo)]])

    return sum(matriz * vector)

def rot_y(vector, angulo):
    ''''
        Dado un vector y los grados, devuelve el vector rotado en el eje Y esa cantidad de grados
    Parameters:
        vector (np.array): vector que se desea rotar en eje Y.
        angulo (float):    grados a rotar el vector.

    Returns:
        np.array: vector girado en el eje y
    '''
    angulo = np.deg2rad(angulo)
    matriz = np.array([[np.cos(angulo), 0, np.sin(angulo)],[0, 1, 0], [-np.sin(angulo), 0, np.cos(angulo)]])

    return sum(matriz * vector)


def rot_z(vector, angulo):
    ''''
        Dado un vector y los grados, devuelve el vector rotado en el eje Z esa cantidad de grados
    Parameters:
        vector (np.array): vector que se desea rotar en eje Z.
        angulo (float):    grados a rotar el vector.

    Returns:
        np.array: vector girado en el eje z
    '''

    angulo = np.deg2rad(angulo)
    matriz = np.array([[np.cos(angulo), -np.sin(angulo), 0], [np.sin(angulo), np.cos(angulo), 0], [0, 0, 1]])

    return sum(vector * matriz)

def rotar(vector, eje, angulo):
    ''''
        Dado un vector, un eje de rotación y los grados, llama a la función de rotación del angulo corresondiente
        y devuelve el vector girado.
    Parameters:
        vector (np.array): vector que se desea rotar en eje X.
        eje    (string):   eje de rotación del vector
        angulo (float):    grados a rotar el vector.

    Returns:
        np.array: vector girado en el eje x
    '''

    if('x' in eje.lower()):
        return rot_x(vector, angulo)
    elif('y' in eje.lower()):
        return rot_y(vector, angulo)
    elif('z' in eje.lower()):
        return rot_z(vector, angulo)


vector = np.array(input('Ingresa un vector de 3 dimensiones con valores enteros o flotantes de la forma: x y z. Ejemplo: 1 2.4 3.0\n').split(' '), np.float128)
eje = input('Ingresa el eje en el que deseas rotar. Ejemplo: Z\n')
angulo = float(input('Ingresa el angulo de rotación en grados:\n'))

vector = rotar(vector, eje, angulo)

print(f'Vector rotado en eje {eje} {angulo} grados.\n{vector}')