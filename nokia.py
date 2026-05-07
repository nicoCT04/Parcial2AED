# Problema 3 - Combinaciones en teclado Nokia 3230
# Disposición del teclado (* y # bloqueadas):
#     [1] [2] [3]
#     [4] [5] [6]
#     [7] [8] [9]
#     [*] [0] [#]

# Vecinos válidos por dígito, incluyendo al propio dígito (consistente con
# el caso n=2 del enunciado, donde 00, 11, ..., 99 forman parte de las 36)
ADYACENCIAS = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [1, 2, 3, 5],
    3: [2, 3, 6],
    4: [1, 4, 5, 7],
    5: [2, 4, 5, 6, 8],
    6: [3, 5, 6, 9],
    7: [4, 7, 8],
    8: [0, 5, 7, 8, 9],
    9: [6, 8, 9],
}

DIGITOS_VALIDOS = range(10)


def construir_tabla_dp(longitud):
    if longitud <= 0:
        return []

    # Caso base: f(1, d) = 1 para cada dígito
    fila_actual = [1] * 10
    tabla_dp = [list(fila_actual)]

    for _ in range(2, longitud + 1):
        # Recurrencia: f(k, d) = suma de f(k-1, v) para cada vecino v de d
        fila_siguiente = [0] * 10
        for digito in DIGITOS_VALIDOS:
            for vecino in ADYACENCIAS[digito]:
                fila_siguiente[digito] += fila_actual[vecino]

        fila_actual = fila_siguiente
        tabla_dp.append(list(fila_actual))

    return tabla_dp


def contar_combinaciones_nokia(longitud):
    tabla_dp = construir_tabla_dp(longitud)
    if not tabla_dp:
        return 0
    fila_final = tabla_dp[-1]
    return sum(fila_final)


def imprimir_tabla_dp(tabla_dp):
    encabezado_digitos = "  ".join(f"d={d:>2}" for d in DIGITOS_VALIDOS)
    print(f"     | {encabezado_digitos}")
    print("     " + "-" * (len(encabezado_digitos) + 2))

    for indice_fila, fila in enumerate(tabla_dp, start=1):
        valores = "  ".join(f"{valor:4d}" for valor in fila)
        print(f"k={indice_fila:2d} | {valores}   total={sum(fila)}")


def main():
    casos_de_prueba = [1, 2, 3, 5, 10]

    for longitud in casos_de_prueba:
        print(f"### n = {longitud} ###")
        tabla = construir_tabla_dp(longitud)
        imprimir_tabla_dp(tabla)
        total = sum(tabla[-1])
        print(f"=> TOTAL DE COMBINACIONES PARA n={longitud}: {total}\n")

main()
