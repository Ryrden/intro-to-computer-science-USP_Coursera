def conta_vogais(frase):  # conta quantos vogais maiúsculas e minúsculas tem na frase

    Numero_vogais = 0
    vogais_min = ['a', 'e', 'i', 'o', 'u']
    vogais_mai = ['A', 'E', 'I', 'O', 'U']

    for i in vogais_min:
        # quantas vogais minúsculas tem
        Numero_vogais = Numero_vogais + frase.count(i)

    for i in vogais_mai:
        # quantas vogais maiúsculas tem
        Numero_vogais = Numero_vogais + frase.count(i)

    return Numero_vogais


def conta_letras(frase, contar='vogais'):

    Numero_consoantes = 0
    caractere_vazio = 0

    if contar == 'vogais':

        Numero_vogais = conta_vogais(frase)

        return Numero_vogais

    elif contar == 'consoantes':

        # contando quando espaços em branco tem no texto
        caractere_vazio = frase.count(' ')

        Numero_vogais = conta_vogais(frase)  # quantas vogais

        Numero_consoantes = len(frase) - Numero_vogais - caractere_vazio 

        return Numero_consoantes

    #Caso seja digitado outra coisa no parâmetro contar 
    return 'não é possível contar quantas ' + contar + ' tem, escolha entre vogais ou consoantes'
