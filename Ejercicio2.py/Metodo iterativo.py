import random

def generar_matriz():
    return [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

def determinante_iterativo(matriz):
    det = 0
    for i in range(len(matriz)):
        product = 1
        for j in range(len(matriz)):
            product *= matriz[j][(i+j) % len(matriz)]
        det += product
        
    for i in range(len(matriz)):
        product = 1
        for j in range(len(matriz)):
            product *= matriz[j][(len(matriz)-1+j-i) % len(matriz)]
        det -= product
        
    return det

# Función principal
def main():
    matriz = generar_matriz()
    print("Matriz:")
    for fila in matriz:
        print(fila)
    det = determinante_iterativo(matriz)
    print("Determinante (Método Iterativo):", det)

if __name__ == "__main__":
    main()
