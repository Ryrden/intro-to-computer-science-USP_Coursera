def soma_matrizes(m1, m2):

    if len(m1) == len(m1): #comparando Linhas

        if len(m1[0]) == len(m2[0]): #comparando Colunas
            lista_final = []
            lista_transporte = [] 

            for i in range(len(m1)): #percorrendo linha
                for j in range(0, len(m1[i])): #percorrendo coluna 
                    aux = 0                      #variável auxiliar para adicionar valores para lista_transporte
                    aux = m1[i][j] + m2[i][j] 
                    lista_transporte.append(aux)
                lista_final.append(lista_transporte)
                lista_transporte = []

            return lista_final

        else:
            return False       #Caso Coluna diferente 
    else:
        return False           #Caso linha diferente
