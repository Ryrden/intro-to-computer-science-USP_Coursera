def cria_matriz(num_linhas, num_colunas, valor):

    Matriz = []  # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        # adiciona linha à matriz
        Matriz.append(linha)

    return Matriz
