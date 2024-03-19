import random

# Función para generar un polinomio aleatorio
def generar_polinomio(grado_maximo):
    polinomio = {}
    grado = random.randint(0, grado_maximo)
    for exp in range(grado, -1, -1):
        coeficiente = random.randint(-10, 10)  # Coeficientes aleatorios entre -10 y 10
        if coeficiente != 0:  # No incluir términos con coeficiente 0
            polinomio[exp] = coeficiente
    return polinomio

# Función para restar dos polinomios
def restar_polinomios(polinomio1, polinomio2):
    resultado = {}
    for exp in polinomio1:
        resultado[exp] = polinomio1[exp]
    for exp in polinomio2:
        if exp in resultado:
            resultado[exp] -= polinomio2[exp]
        else:
            resultado[exp] = -polinomio2[exp]
    return resultado

# Función para dividir dos polinomios
def dividir_polinomios(polinomio1, polinomio2):
    if not polinomio2:
        raise ValueError("El divisor no puede ser un polinomio vacío")
    cociente = {}
    residuo = dict(polinomio1)
    while residuo and max(residuo) >= max(polinomio2):
        coeficiente = residuo[max(residuo)] / polinomio2[max(polinomio2)]
        exp = max(residuo) - max(polinomio2)
        cociente[exp] = coeficiente
        for k in polinomio2:
            if exp + k in residuo:
                residuo[exp + k] -= polinomio2[k] * coeficiente
            else:
                residuo[exp + k] = -polinomio2[k] * coeficiente
        del residuo[max(residuo)]
    return cociente, residuo

# Función para eliminar un término de un polinomio
def eliminar_termino(polinomio, exponente):
    if exponente in polinomio:
        del polinomio[exponente]
        return polinomio
    else:
        return polinomio

# Función para determinar si un término específico existe en un polinomio
def termino_existe(polinomio, exponente):
    return exponente in polinomio

# Generar dos polinomios aleatorios
polinomio1 = generar_polinomio(5)
polinomio2 = generar_polinomio(5)

# Mostrar los polinomios generados
print("Polinomio 1:", polinomio1)
print("Polinomio 2:", polinomio2)

# Restar los polinomios
resultado_resta = restar_polinomios(polinomio1, polinomio2)
print("Resultado de la resta:", resultado_resta)

# Dividir los polinomios
cociente, residuo = dividir_polinomios(polinomio1, polinomio2)
print("Cociente de la división:", cociente)
print("Residuo de la división:", residuo)

# Eliminar un término del primer polinomio
exponente_a_eliminar = random.choice(list(polinomio1.keys()))
polinomio1_actualizado = eliminar_termino(polinomio1, exponente_a_eliminar)
print(f"Polinomio 1 después de eliminar el término con exponente {exponente_a_eliminar}:", polinomio1_actualizado)

# Determinar si un término específico existe en el primer polinomio
exponente_a_buscar = random.randint(0, 5)
print(f"¿El término con exponente {exponente_a_buscar} existe en el polinomio 1?:", termino_existe(polinomio1, exponente_a_buscar))
