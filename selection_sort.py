def selection_sort(lista):
    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]

    return lista
