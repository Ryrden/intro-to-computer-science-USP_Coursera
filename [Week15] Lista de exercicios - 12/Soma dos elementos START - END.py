def soma_lista(lista):

    primeiro = lista[0] #BASE DA RECURSÂO

    if len(lista) == 1:
        return primeiro

    del(lista[0])

    return primeiro + soma_lista(lista) #CHAMADA DA RECURSÃO