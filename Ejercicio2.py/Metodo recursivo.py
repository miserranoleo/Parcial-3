import random

def generar_matriz():
    return [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

def determinante_recursivo(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    elif len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for j in range(len(matriz)):
            det += (-1) ** j * matriz[0][j] * determinante_recursivo(submatriz(matriz, 0, j))
        return det

def submatriz(matriz, i, j):
    return [fila[:j] + fila[j+1:] for fila in (matriz[:i] + matriz[i+1:])]

# Función principal
def main():
    matriz = generar_matriz()
    print("Matriz:")
    for fila in matriz:
        print(fila)
    det = determinante_recursivo(matriz)
    print("Determinante (Método Recursivo):", det)

if __name__ == "__main__":
    main()
