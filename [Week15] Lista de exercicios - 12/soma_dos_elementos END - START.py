def soma_lista(lista):

    if len(lista) == 1:  #BASE DA RECURSÂO
        return lista[0]
    
    ultimo = lista[-1]

    del(lista[-1])
    
    return ultimo + soma_lista(lista) #CHAMADA DA RECURSÃO