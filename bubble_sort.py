def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)
    trocas = 0

    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, trocas
