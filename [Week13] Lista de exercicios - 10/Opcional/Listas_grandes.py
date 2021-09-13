import random

def lista_grande(n):
    # Aprendendo a mexer com o módulo random
    lista = []

    for i in range(n):
        numero_aleatorio = random.randint(1,100)
        
        lista.append(numero_aleatorio)

    return lista

# Verificação
if __name__ == "__main__":

    print(lista_grande(5))
    print(lista_grande(10))
    print(lista_grande(15))
