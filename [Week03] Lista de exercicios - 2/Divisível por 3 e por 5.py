valor = int(input("Digite um número inteiro: "))

Multiplo_de_5 = valor % 5
Multiplo_de_3 = valor % 3

if (Multiplo_de_5 == 0 and Multiplo_de_3 == 0):
    print("FizzBuzz")
else:
    print(valor)