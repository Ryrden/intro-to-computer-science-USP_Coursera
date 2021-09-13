def ordena(lista):

    Endlist = len(lista)

    for i in range(Endlist-1):

        Menor_posição = i

        for j in range(i+1, Endlist):
            if lista[j] < lista[Menor_posição]:
                Menor_posição = j

        lista[i], lista[Menor_posição] = lista[Menor_posição], lista[i]

    return lista


# Verificação
if __name__ == "__main__":

    # Trouxe a função pelo fato de quanto se importa em módulo, aparece outros dois arquivos gerados automaticamente
    def lista_grande(n):

        import random

        lista = []

        for i in range(n):
            numero_aleatorio = random.randint(1, 100)

            lista.append(numero_aleatorio)

        return lista

    lista = lista_grande(10)

    print(
        f"Antes de ser Ordenada \t-> {lista}\n\n"
        f"Depois de ser Ordenada \t-> {ordena(lista)}"
    )
