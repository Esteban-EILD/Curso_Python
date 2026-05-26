voltaje = int(input("Ingrese la cantidad de voltaje: "))
if voltaje < 110:
    print("\n Alerta.Subtensión en la red.")
elif 110 <= voltaje <= 220:
    print("\n Operación estable.")
elif voltaje > 220:
    print("\n Peligro: Sobretensión detectada.")
estado = "Crítico" if (110 > voltaje or voltaje > 220) else "Estable"
print("\n Estado del sistema:", estado)