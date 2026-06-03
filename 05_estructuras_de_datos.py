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