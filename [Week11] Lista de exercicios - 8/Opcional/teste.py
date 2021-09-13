lista = ['maria', 'josé', 'PAULO', 'Catarina']

lista2 = []
cont = 122

for palavra in lista:

    ordem_lexico = 65

    while ordem_lexico <= cont:

        if ord(palavra[0]) == ordem_lexico:
            lista2.append(palavra)

        ordem_lexico += 1
