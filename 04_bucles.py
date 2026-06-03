energy=100 # Variable de control
while energy > 0:
    energy -= 15
    print("\n Energía restante:", energy)
print("\n La energía se ha agotado.")

for i in range(5, 31, 5):
    print("\n Múltiplos de 5 entre 5 y 30:", i)
    
# --- Experimento con Modificadores de Flujo ---
print("\n--- Demostración de break y continue ---")

for numero in range(1, 10):
    if numero == 3:
        print("Saltando el 3 con 'continue'")
        continue  # Salta directo a la siguiente vuelta del ciclo
        
    if numero == 7:
        print("Abortando el ciclo en 7 con 'break'")
        break  # Rompe el bucle por completo
        
    print("Número actual:", numero)
    
"""Este código muestra cómo usar 'break' para salir de un bucle y
'continue' para saltar a la siguiente iteración. En este caso,
el número 3 se salta y el ciclo se detiene completamente al
llegar al número 7."""