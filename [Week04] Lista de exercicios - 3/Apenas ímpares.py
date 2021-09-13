valor = int(input("Digite um numero: "))
 
x = 0

while not valor == 0:
    
    k = x % 2
    x = x + 1  

    if  not k == 1:
        print(x)
        valor = valor - 1