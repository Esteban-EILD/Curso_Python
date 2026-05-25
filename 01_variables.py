# --- Explorando Tipos de Datos y Precisión ---

# 1. Entero de precisión arbitraria (¡no se desborda!)
factorial_grande = 123456789012345678901234567890
print("Tipo de entero:", type(factorial_grande))

# 2. El misterio de los flotantes
operacion = 0.1 + 0.2
print("\n¿Cuánto es 0.1 + 0.2 según Python?:", operacion)
print("¿Es exactamente igual a 0.3?:", operacion == 0.3)

# 3. Cadenas y su inmutabilidad
institucion = "Escuela Politécnica Nacional"
# Las cadenas se pueden indexar. Vamos a extraer las siglas "EPN" usando rebanado (slicing)
# Tomamos los caracteres en las posiciones 0, 8 y 20
siglas = institucion[0] + institucion[8] + institucion[20]
print("\nExtracción de texto:", siglas)