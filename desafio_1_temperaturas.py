# ==============================================================================
# DESAFÍO 1: Conversor de Temperaturas Interactivo (Versión Local)
# OBJETIVO: Escribir un programa que convierta temperaturas entre Celsius,
#           Fahrenheit y Kelvin utilizando funciones y condicionales.
# ==============================================================================

# ------------------------------------------------------------------------------
# PASO 1: Definir las funciones de conversión matemática.
# ------------------------------------------------------------------------------

def celsius_a_fahrenheit(celsius: float) -> float:
    resultado_fahrenheit = (celsius * 9/5) + 32
    return resultado_fahrenheit

def celsius_a_kelvin(celsius: float) -> float:
    resultado_kelvin = celsius + 273.15
    return resultado_kelvin


# ------------------------------------------------------------------------------
# PASO 2: Crear la función principal que controlará el flujo del programa.
# ------------------------------------------------------------------------------

def menu_conversor():
    print("=== BIENVENIDO AL CONVERSOR CIENTÍFICO DE TEMPERATURAS ===")
    
    # 1. Solicitar al usuario que ingrese la temperatura en Celsius de forma interactiva
    celsius = float(input("Ingresa la temperatura en °C: "))
    
    print("\n¿A qué unidad deseas convertir?")
    print("1. Fahrenheit")
    print("2. Kelvin")
    print("3. Ambas")
    
    # 2. Solicitar la opción del menú
    opcion = input("Elige una opción (1-3): ")
    
    # 3. Evaluar la opción ingresada usando condicionales
    if opcion == "1":
        f = celsius_a_fahrenheit(celsius)
        print(f"\n-> La conversión de {celsius:.2f}°C a Fahrenheit es: {f:.2f}°F")
        
    elif opcion == "2":
        k = celsius_a_kelvin(celsius)
        print(f"\n-> La conversión de {celsius:.2f}°C a Kelvin es: {k:.2f}°K")
        
    elif opcion == "3":
        f = celsius_a_fahrenheit(celsius)
        k = celsius_a_kelvin(celsius)
        print(f"\n-> {celsius:.2f}°C equivale a:")
        print(f"   * {f:.2f}°F")
        print(f"   * {k:.2f}°K")
        
    else:
        print("\n-> Error: Opción no válida. Por favor, selecciona 1, 2 o 3.")


# ------------------------------------------------------------------------------
# PASO 3: Punto de entrada para ejecutar el programa.
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    menu_conversor()

