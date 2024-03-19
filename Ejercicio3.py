naves = [
    {"nombre": "Cometa Veloz", "longitud": 50, "tripulantes": 10, "pasajeros": 100},
    {"nombre": "Titán del Cosmos", "longitud": 100, "tripulantes": 20, "pasajeros": 200},
    {"nombre": "Millennium Falcon", "longitud": 50, "tripulantes": 10, "pasajeros": 100},
    {"nombre": "USS Enterprise", "longitud": 100, "tripulantes": 20, "pasajeros": 200},
    {"nombre": "Serenity", "longitud": 80, "tripulantes": 15, "pasajeros": 150},
    {"nombre": "Event Horizon", "longitud": 70, "tripulantes": 12, "pasajeros": 120},
    {"nombre": "Heart of Gold", "longitud": 120, "tripulantes": 25, "pasajeros": 250},
]

# Ordenar la lista de naves por nombre de forma ascendente y por longitud de forma descendente.
naves_ordenadas = sorted(naves, key=lambda x: (x['nombre'], -x['longitud']))

# Mostrar toda la información de las naves "Cometa Veloz" y "Titán del Cosmos".
print("• Información de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
for nave in naves_ordenadas:
    if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]:
        print("- Nombre:", nave["nombre"])
        print("  Longitud:", nave["longitud"])
        print("  Tripulantes:", nave["tripulantes"])
        print("  Pasajeros:", nave["pasajeros"])

# Determinar cuáles son las cinco naves con mayor cantidad de pasajeros.
naves_mayor_pasajeros = sorted(naves, key=lambda x: x['pasajeros'], reverse=True)[:5]
print("\n• Las cinco naves con mayor cantidad de pasajeros son:")
for nave in naves_mayor_pasajeros:
    print("-", nave["nombre"])

# Indicar cuál es la nave que requiere la mayor cantidad de tripulación.
nave_mayor_tripulacion = max(naves, key=lambda x: x['tripulantes'])
print("\n• La nave que requiere la mayor cantidad de tripulación es:", nave_mayor_tripulacion["nombre"])

# Mostrar todas las naves cuyo nombre comience con "GX".
naves_nombre_gx = [nave for nave in naves if nave["nombre"].startswith("GX")]
print("\n• Las naves cuyo nombre comienza con 'GX' son:")
for nave in naves_nombre_gx:
    print("-", nave["nombre"])

# Listar todas las naves que pueden llevar seis o más pasajeros.
naves_seis_o_mas_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]
print("\n• Las naves que pueden llevar seis o más pasajeros son:")
for nave in naves_seis_o_mas_pasajeros:
    print("-", nave["nombre"])

# Mostrar toda la información de la nave más pequeña y la más grande.
nave_mas_pequena = min(naves, key=lambda x: x['longitud'])
nave_mas_grande = max(naves, key=lambda x: x['longitud'])
print("\n• La nave más pequeña es:", nave_mas_pequena)
print("\n• La nave más grande es:", nave_mas_grande)
