import random

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort


def gerar_lista(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]


if __name__ == "__main__":
    numeros = gerar_lista(15)
    print("lista original:", numeros)

    ordenado_bubble, trocas_bubble = bubble_sort(numeros)
    ordenado_selection, trocas_selection = selection_sort(numeros)
    ordenado_insertion, trocas_insertion = insertion_sort(numeros)

    print("\nbubble sort:", ordenado_bubble)
    print("selection sort:", ordenado_selection)
    print("insertion sort:", ordenado_insertion)

    print("\ncomparativo de trocas:")
    print("bubble sort:", trocas_bubble)
    print("selection sort:", trocas_selection)
    print("insertion sort:", trocas_insertion)
