def maiusculas(frase):
    cont = 0    #contador para localização da String dada 
    Maiusculas = '' 

    while cont < len(frase): #Percorrer a String

        if ord(frase[cont]) >= 65 and ord(frase[cont]) <= 90: #Se a letra da String é Maiscula de acordo com a tabela ORD
            Maiusculas = Maiusculas + frase[cont]
        
        cont += 1

    return Maiusculas


def Testa_M(): # Testando a Função

    if maiusculas('Programamos em python 2?') == 'P':
        print("ok")
    
    if maiusculas('Programamos em Python 3.') == 'PP':
        print("ok2")

    if maiusculas('PrOgRaMaMoS em python!') == 'PORMMS':
        print("ok3")

