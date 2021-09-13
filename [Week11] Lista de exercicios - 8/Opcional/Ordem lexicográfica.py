def primeiro_lex(lista):

    lista2 = []
    menor_ordem = 65
    ordem_lexico = 122

    for palavra in lista:  # percorrendo lista

        while ordem_lexico >= menor_ordem:  # enquanto a ordem lexicográfica for maior que a definida

            if ord(palavra[0]) <= ordem_lexico:
                lista2.insert(0, palavra)
                # definindo menor ordem lexicográfica checada até agora
                ordem_lexico = ord(palavra[0])
                break

            ordem_lexico -= 1

    return str(lista2[0])


print(primeiro_lex('ABC'))
