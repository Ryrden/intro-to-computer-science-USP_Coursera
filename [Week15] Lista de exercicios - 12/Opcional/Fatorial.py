def fatorial(x):

    if x <= 1: #Base da Recursão
        return 1

    return x * fatorial(x-1) #Chamada da recursão