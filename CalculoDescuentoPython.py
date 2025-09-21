def calcular_descuento(monto_total, descuento=10):  # Valor por defecto del 10%

    # Calcula el monto del descuento
    monto_descuento = (descuento / 100) * monto_total
    return monto_descuento


# Uso de la función
# Primera llamada: solo monto total (usa descuento por defecto = 10%)
compra1 = float(input("Ingrese el monto total de la compra 1: "))
descuento1 = calcular_descuento(compra1)  # aplica 10% por defecto
final1 = compra1 - descuento1
print("\n--- Compra 1 ---")
print(f"Monto total antes del descuento: ${compra1}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${final1:.2f}")

# Segunda llamada: monto total + porcentaje de descuento específico
compra2 = float(input("\nIngrese el monto total de la compra 2: "))
descuento2 = calcular_descuento(compra2, 15)  # aplica 15%
final2 = compra2 - descuento2
print("\n--- Compra 2 ---")
print(f"Monto total antes del descuento: ${compra2}")
print(f"Descuento aplicado (15%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${final2:.2f}")
