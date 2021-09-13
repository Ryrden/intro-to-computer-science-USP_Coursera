def bubble_sort(lista):

    fim = len(lista)

    for i in range(fim-1, 0, -1):
        trocou = False

        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)
        if trocou == False:
            return lista

    return lista
