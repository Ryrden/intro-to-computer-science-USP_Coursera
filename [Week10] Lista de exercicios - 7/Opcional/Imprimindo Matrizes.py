def imprime_matriz(matriz):

    for i in range(len(matriz)):  # percorrendo linha

        for j in range(0, len(matriz[i])):  # percorrendo coluna

            if j < len(matriz[i]) - 1:
                print(matriz[i][j], end=" ")

            else:
                print(matriz[i][j])
