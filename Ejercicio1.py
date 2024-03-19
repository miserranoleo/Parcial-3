import random
def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Mover n-1 piedras de la fuente al auxiliar usando el destino como auxiliar
        hanoi(n-1, source, auxiliary, target)
        
        # Mover la n-ésima piedra de la fuente al destino
        print(f"Move disk {n} from source {source} to destination {target}")
        
        # Mover n-1 piedras del auxiliar al destino usando la fuente como auxiliar
        hanoi(n-1, auxiliary, target, source)

# Función principal
def main():
    num_piedras = random.randint(0, 10)
    pila_A = 'A'
    pila_B = 'B'
    pila_C = 'C'
    
    # Llamar a la función hanoi para resolver el problema
    hanoi(num_piedras, pila_A, pila_C, pila_B)

if __name__ == "__main__":
    main()

