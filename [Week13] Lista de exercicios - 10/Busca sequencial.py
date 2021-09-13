def busca(lista, elemento):

    EndList = len(lista)

    for i in range(EndList):
        if lista[i] == elemento:
            return i
    return False


# Verificação
if __name__ == "__main__":

    assert busca(['a', 'e', 'i'], 'e') == 1
    assert busca([12, 13, 14], 15) == False
    assert busca([1, 20, 40, 'a', 32, 70], 70) == 5
