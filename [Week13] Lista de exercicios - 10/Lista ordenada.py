def ordenada(lista):

    fim_list = len(lista)

    for i in range(fim_list - 1):
        if lista[i] > lista[i+1]:
            return False
    
    return True
