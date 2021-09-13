lista = [2,4,2,2,3,3,1]
def remove_repetidos(lista):
    lista2 = []

    z = sorted(lista)

    for x in range(len(lista)):
        if not z[x] == z[x-1]:
            lista2.append(z[x])

    return lista2
