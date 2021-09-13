valor = int(input("Digite um valor: "))

i = 2
aux = 0

if (valor != 1 and valor != 0): #me sinto mal por usar um IF para isso
    while i < valor: 
        x = valor % i
        i = i + 1
        if (x == 0):
            aux = 1
else:
    aux = 1

if (aux == 1):
    print("não primo")
else:
    print("primo")