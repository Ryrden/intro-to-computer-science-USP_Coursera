lista = []
z = 1
while z != 0:
    z = (int(input("Digite um número: ")))  
    lista.append(z)

tam = len(lista) - 2

while tam >= 0:
    print(lista[tam])
    tam = tam - 1