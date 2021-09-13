def encontra_impares(lista):
    primeiro_item = lista[0]

    if len(lista) == 1:  # BASE DA RECURSÃO
        if primeiro_item % 2 == 1:
            return [primeiro_item]
        else:
            return []

    del(lista[0])

    if primeiro_item % 2 == 1:
        # CHAMADA DA RECURSÃO CASO SEJA IMPAR
        return [primeiro_item] + encontra_impares(lista)

    return encontra_impares(lista)  # CHAMADA DA RECURSÃO CASO SEJA PAR


if __name__ == "__main__":

    assert encontra_impares([5, 5, 5, 54, 2, 6]) == [5, 5, 5]

    assert encontra_impares([
        54, 265, 2154, 25, 1, 50,
        45, 15, 0, 60, 651, 4, 65,
        51, 51, 5
    ]) == [265, 25, 1, 45, 15, 651, 65, 51, 51, 5]

