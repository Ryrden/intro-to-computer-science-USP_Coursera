def insertion_sort(lista):

    fim = len(lista) 

    for i in range(1, fim): #A partir do 2 item da lista

        for j in range(i, 0, -1):  #percorrendo do item da lista até o começo dela
            trocou = False
            if lista[i] < lista[j-1]: #Comparando se o item da lista é menor que seu antecessor
                lista[i], lista[j-1] = lista[j-1], lista[i] #Trocando posições
                i -= 1 
                trocou = True

            if trocou == False:
                break

    return lista
