import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    #Grau de similiaridade entre textos
    S_ab = []
    for x in range(len(as_a)):
        diferença = abs(as_a[x] - as_b[x])
        S_ab.append(diferença)

    return S_ab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
   #Separando frases das sentenças e palavras das frases
    lista_frases = []
    lista_palavras = []
    sentencas = separa_sentencas(texto)

    for x in sentencas:
        new_frases = separa_frases(x)
        lista_frases.extend(new_frases)

    for x in lista_frases:
        new_palavras = separa_palavras(x)
        lista_palavras.extend(new_palavras)

   #variáveis "Total"
    Total_de_sentenças = len(sentencas)
    Total_de_frases = len(lista_frases)
    Total_de_palavras = len(lista_palavras)

   #Tamanho médio das palavras
    Total_de_letras = 0 
    for y in lista_palavras:
        nº_letras = len(y)
        Total_de_letras += nº_letras

    tmp = Total_de_letras / Total_de_palavras

   #Relação Type-Token
    palavras_diferentes = n_palavras_diferentes(lista_palavras)

    rtt = palavras_diferentes / Total_de_palavras

   #Razão Hapax Legomana
    palavras_unicas = n_palavras_unicas(lista_palavras)

    rhl = palavras_unicas / Total_de_palavras

   #Tamanho médio de sentença
    Caracteres_totais_de_sentença = 0
    for y in sentencas:
        new_caracteres_Sent = len(y) 
        Caracteres_totais_de_sentença = Caracteres_totais_de_sentença + new_caracteres_Sent

    tms = Caracteres_totais_de_sentença / Total_de_sentenças

   #Complexidade de sentença

    cds = Total_de_frases / Total_de_sentenças

   #Tamanho médio de frase
    Caracteres_totais_de_frases = 0
    for y in lista_frases:
        new_caracteres_frases = len(y)
        Caracteres_totais_de_frases = Caracteres_totais_de_frases + new_caracteres_frases

    tmf = Caracteres_totais_de_frases / Total_de_frases
    
   #FIM
    return [tmp, rtt, rhl, tms, cds, tmf]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista_comparação = []

    for i in range(len(textos)):
        Texto_avaliado = calcula_assinatura(textos[i])
        for x in range(len(Texto_avaliado)):
            fita = compara_assinatura(ass_cp, Texto_avaliado)
            similiaridade = (Texto_avaliado[x] + fita[x]) / 6
            comparação = ass_cp[x] - similiaridade
            lista_comparação.append(comparação)

            if ass_cp[x] >= similiaridade:
                if comparação <= lista_comparação[x-1]:
                    resultado = i

    return resultado

def Main():
    CohPiah = le_assinatura()
    Textos = le_textos()
    text = calcula_assinatura(Textos)
    compara_assinatura(CohPiah, text)
    avalia_textos(Textos, CohPiah)

Main()