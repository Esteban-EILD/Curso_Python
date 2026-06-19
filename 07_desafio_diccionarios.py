# --- Base de Datos de Telemetría ---
nodos_computo = {
    "Nodo_Alpha": [65, 72, 88, 92, 70],
    "Nodo_Beta": [55, 60, 58, 62, 61],
    "Nodo_Gamma": [78, 85, 95, 102, 89],
    "Nodo_Delta": [62, 64, 68, 65, 63]
}
# Si encuentra una falla, rompe el bucle y NO entra al else
for clave, valor in nodos_computo.items():
    falla = False
    for temperatura in valor:
        if temperatura > 90:
            print(f"\n Alerta: nodo {clave} tiene temperatura crítica de {temperatura}")
            falla = True
            break # Rompe el bucle interno
    if falla:
        break # Rompe el bucle externo
else:
    # Este bloque pertenece al 'for' principal. 
    # Solo se ejecuta si NINGÚN break se activó.
    print("\n Sistema operando con temperaturas estables")
