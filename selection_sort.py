def selection_sort(lista):
    lista = lista.copy()
    n = len(lista)
    trocas = 0

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        # so troca se achou alguem menor, senao fica trocando com ele mesmo
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1

    return lista, trocas
