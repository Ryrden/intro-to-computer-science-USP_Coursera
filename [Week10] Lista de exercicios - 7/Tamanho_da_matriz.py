def dimensoes(matriz):
    colunas = 0

    linhas = len(matriz)  # Quantas linhas tem

    for in matriz[0]:  # Quantas colunas tem
        colunas += 1

    print(linhas, 'X', colunas, sep='')
