# Problema 1 - Hacer Sencillo (Coin Change)
# Análisis y Diseño de Algoritmos - UVG, Examen Parcial #2

DENOMINACIONES_CENTAVOS = (25, 10, 5, 1)


def hacer_sencillo(monto_centavos, denominaciones=DENOMINACIONES_CENTAVOS):
    if monto_centavos < 0:
        raise ValueError("El monto no puede ser negativo")

    # Greedy-choice: probar primero la denominación más grande
    denominaciones_descendentes = sorted(denominaciones, reverse=True)

    monedas_usadas = []
    restante = monto_centavos

    for denominacion in denominaciones_descendentes:
        if restante == 0:
            break
        cantidad = restante // denominacion
        if cantidad > 0:
            monedas_usadas.append((denominacion, cantidad))
            restante -= cantidad * denominacion

    return monedas_usadas


def contar_monedas_totales(solucion):
    return sum(cantidad for _, cantidad in solucion)


def imprimir_solucion(monto_centavos, solucion):
    monto_quetzales = monto_centavos / 100
    total = contar_monedas_totales(solucion)

    print(f"Monto: Q{monto_quetzales:.2f} ({monto_centavos} centavos)")
    for denominacion, cantidad in solucion:
        print(f"  {cantidad:3d} moneda(s) de {denominacion:2d} centavos")
    print(f"  TOTAL: {total} monedas\n")


def main():
    casos_de_prueba = [
        ("Caso del enunciado (Q2.93)", 293),
        ("Monto pequeño",               87),
        ("Monto trivial (1 centavo)",    1),
        ("Monto grande",               999),
    ]

    for descripcion, monto in casos_de_prueba:
        print(f"### {descripcion} ###")
        solucion = hacer_sencillo(monto)
        imprimir_solucion(monto, solucion)

main()