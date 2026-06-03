temperaturas = [18.5, 22.4, 19.1]
coordenadas = (-1.67, -78.65)
temperaturas[0]= 20.0
# --- Métodos Esenciales de Listas ---
print("Lista original:", temperaturas)

# 1. .append(elemento) -> Añade un objeto al final de la lista
temperaturas.append(24.2)
print("Luego de .append():", temperaturas)

# 2. .insert(índice, elemento) -> Inserta un objeto en una posición específica
temperaturas.insert(1, 15.0)
print("Luego de .insert() en índice 1:", temperaturas)

# 3. .remove(valor) -> Busca y elimina la primera coincidencia de ese valor
temperaturas.remove(22.4)
print("Luego de .remove(22.4):", temperaturas)

# 4. .pop() -> Elimina el último elemento de la lista y la devuelve
ultimo = temperaturas.pop()
print("Luego de .pop() (se eliminó:", ultimo, "):", temperaturas)

# --- Demostración de Slicing ---
valores = [0, 10, 20, 30, 40, 50, 60]

# Extraer del índice 1 al 4 (recuerda: el 5 queda fuera)
sub_conjunto = valores[1:5] 
print("\nSlicing valores[1:5]:", sub_conjunto) # Debería dar [10, 20, 30, 40]

# --- Desafío de Integración: Filtrado de Datos ---
print("\n--- Procesamiento de Señales ---")

voltajes = [120, 85, 230, 115, 50, 195, 240]
voltajes_estables = []

# Tu tarea: 
# Recorre la lista de 'voltajes' usando un bucle for.
# Si el voltaje se encuentra en el rango estable (entre 110 y 220 inclusive), 
# añádelo a la lista 'voltajes_estables' usando el método .append().
# Al final, imprime la lista de voltajes estables filtrados.
for v_estable in voltajes:
    if 110 <= v_estable <= 220:
        voltajes_estables.append(v_estable)

print("Voltajes estables:", voltajes_estables)

# --- Desafío de Integración: Limpieza y Clasificación de Datos ---
datos_sucios = [65, "error", 88, 42, "nulo", 95, 30, "revisar", 71]

notas_aprobatorias = []
notas_reprobatorias = []

for elemento in datos_sucios:
    if isinstance(elemento, int):
        # Sumamos 5 puntos asegurando un tope máximo de 100
        nota_con_bono = min(elemento + 5, 100)
        
        # Clasificamos directamente en el mismo bucle
        if nota_con_bono >= 60:
            notas_aprobatorias.append(nota_con_bono)
        else:
            notas_reprobatorias.append(nota_con_bono)

# Imprimimos una sola vez al final del programa
print("Notas aprobatorias:", notas_aprobatorias)
print("Notas reprobatorias:", notas_reprobatorias)
