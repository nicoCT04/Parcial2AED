# Problema 2 - Knapsack Fraccionado

from dataclasses import dataclass


@dataclass
class Articulo:
    nombre: str
    peso_disponible: float
    precio_total: float

    @property
    def valor_por_unidad(self):
        return self.precio_total / self.peso_disponible


@dataclass
class CantidadRobada:
    nombre: str
    cantidad: float
    valor_obtenido: float


def resolver_knapsack_fraccionado(articulos, capacidad_mochila):
    if capacidad_mochila < 0:
        raise ValueError("La capacidad de la mochila no puede ser negativa")
    for articulo in articulos:
        if articulo.peso_disponible <= 0:
            raise ValueError(
                f"El peso disponible del artículo '{articulo.nombre}' "
                f"debe ser positivo")

    # Greedy-choice: ordenar por valor por unidad de peso, descendente
    articulos_ordenados = sorted(
        articulos,
        key=lambda a: a.valor_por_unidad,
        reverse=True
    )

    espacio_restante = capacidad_mochila
    valor_total = 0.0
    cantidades_robadas = []

    for articulo in articulos_ordenados:
        if espacio_restante == 0:
            break

        cantidad_a_tomar = min(articulo.peso_disponible, espacio_restante)
        valor_obtenido = cantidad_a_tomar * articulo.valor_por_unidad

        cantidades_robadas.append(CantidadRobada(
            nombre=articulo.nombre,
            cantidad=cantidad_a_tomar,
            valor_obtenido=valor_obtenido,
        ))

        valor_total += valor_obtenido
        espacio_restante -= cantidad_a_tomar

    return valor_total, cantidades_robadas


def imprimir_resultado(capacidad_mochila, articulos, valor_total, cantidades_robadas):
    print(f"Capacidad de la mochila: W = {capacidad_mochila}")
    print("Artículos disponibles:")
    for articulo in articulos:
        print(f"  {articulo.nombre}: peso={articulo.peso_disponible}, "
            f"precio=${articulo.precio_total}, "
            f"v/u=${articulo.valor_por_unidad:.2f}")

    print("Solución:")
    for robado in cantidades_robadas:
        print(f"  Tomar {robado.cantidad} unidades de {robado.nombre} "
            f"(${robado.valor_obtenido:.2f})")
    print(f"VALOR TOTAL: ${valor_total:.2f}\n")


def main():
    articulos_enunciado = [
        Articulo("item1", peso_disponible=10, precio_total=60),
        Articulo("item2", peso_disponible=20, precio_total=100),
        Articulo("item3", peso_disponible=30, precio_total=120),
    ]

    casos_de_prueba = [
        ("Caso del enunciado (W=50)", articulos_enunciado, 50),
        ("Mochila pequeña (W=5)",      articulos_enunciado,  5),
        ("Mochila enorme (W=100)",     articulos_enunciado, 100),
    ]

    for descripcion, articulos, capacidad in casos_de_prueba:
        print(f"### {descripcion} ###")
        valor, robadas = resolver_knapsack_fraccionado(articulos, capacidad)
        imprimir_resultado(capacidad, articulos, valor, robadas)

main()