def menor_nome(nomes):

    # primeira palavra definida caso todas tenham o mesmo comprimento
    menor_lista = [nomes[0]]
    tamanho = len(nomes[0])  # tamanho da 1º palavra da lista

    for i in range(len(nomes)):  # percorrendo lista

        # variável auxiliar para nome percorrido ++ sem espaços
        aux = nomes[i].strip()

        if len(aux) < tamanho:  # se o tamanho da palavra atual é menor que a primeira da lista
            menor_lista.append(aux)

        # atualizando tamanho para palavra percorrida (anterior na próxima verificação)
        tamanho = len(aux)

    # último nome adicionado na lista com a primeira letra Maiúscula
    Nome_final = str(menor_lista[-1].capitalize())

    return Nome_final

def testa_menor_nome():  # TESTADOR
    if menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José':
        print("ok1")

    if menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José':
        print("ok2")

    if menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José':
        print('ok3')

    if menor_nome(['zé', ' lu', 'fê']) == 'zé':
        print('ok4')