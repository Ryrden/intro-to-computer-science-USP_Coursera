valor = int(input("Digite um valor: "))

aux = 0

while valor > 0:
    ultimo = valor % 10
    valor //= 10
    penultimo = valor % 10
    if ultimo == penultimo:
        aux = 1

if aux:
    print("sim")
else:
    print("não")