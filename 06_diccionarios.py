sensor_optimizacion = {
    "id":"OPT-2026",
    "frecuencia_hz":2500,
    "variables_monitoreo":["voltaje", "temperatura", "impedancia"],
    "estado_critico":False
}
print(sensor_optimizacion)

# --- Operaciones de Lectura y Escritura ---
print("\n--- Manipulando Datos del Sensor ---")

# 1. Intenta leer de forma segura una clave inexistente usando .get()
resolucion = sensor_optimizacion.get("resolución", "Estándar de fábrica")
print("Resolución del sistema:", resolucion)

# 2. Modifica el estado crítico a True
sensor_optimizacion["estado_critico"] = True

# 3. Añade una nueva clave llamada "precisión" con el valor flotante 0.99
sensor_optimizacion["precisión"] = 0.99

# 4. Imprime el diccionario final actualizado
print("\nDiccionario actualizado:")
print(sensor_optimizacion)

# --- Métodos de Iteración ---
print("\n--- Extrayendo componentes con bucles ---")

# Enfoque 1: Recorrer solo las CLAVES (.keys())
print("1. Iterando por Claves:")
for clave in sensor_optimizacion.keys():
    print("-> Clave encontrada:", clave)

# Enfoque 2: Recorrer solo los VALORES (.values())
print("\n2. Iterando por Valores:")
for valor in sensor_optimizacion.values():
    print("-> Valor almacenado:", valor)

# Enfoque 3: Recorrer AMBOS al mismo tiempo (.items()) -> El más usado
print("\n3. Desempaquetado completo (Clave-Valor):")
for clave, valor in sensor_optimizacion.items():
    print(f"Mapeo: [{clave}] asociado a -> {valor}")