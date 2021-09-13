valor = int(input("Digite um valor: "))

soma = 0

while (valor > 0):
    x = valor // 10
    k = valor % 10
    soma = k + soma
    valor = valor // 10

print(soma)