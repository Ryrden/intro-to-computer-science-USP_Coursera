# Código feito de outra maneira mas está funcionando perfeitamente, isso é ótimo!

def busca(lista_ord, elemento_procurado):
    primeiro = 0
    ultimo = len(lista_ord) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        elemento = lista_ord[meio]
        print(meio)

        if elemento < elemento_procurado:
            primeiro = meio + 1

        elif elemento > elemento_procurado:
            ultimo = meio - 1

        else:
            return meio

    return False
