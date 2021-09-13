import math
from os import system


def delta(a, b, c):
    return (b**2) - (4*a*c)


def EncontraRaiz():
    a_digitado = float(input("dado ax²+ bx + c = 0 Defina o valor de a: "))
    b_digitado = float(input("dado ax²+ bx + c = 0 Defina o valor de b: "))
    c_digitado = float(input("dado ax²+ bx + c = 0 Defina o valor de c: "))
    imprime_raizes(a_digitado, b_digitado, c_digitado)


def imprime_raizes(a, b, c):
    if (a != 0 and b != 0 and c == 0):
        if b > 0:
            print(f"suas duas raizes são x1 = 0 e x2 = {b}")
        else:
            print(f"suas duas raizes são x1 = {b} e x2 = 0")

    elif (a != 0 and b == 0 and c != 0):
        print(
            f"suas duas raizes são x1 = -{math.sqrt(c)} e x2 = +{math.sqrt(c)}")

    elif (a != 0 and b != 0 and c != 0):

        d = delta(a, b, c)
        raiz = math.sqrt(d)
        x1 = (-(b) + raiz)/(2*a)
        x2 = (-(b) - raiz)/(2*a)
        if (d > 0):
            print("você tem duas raizes distintas")
            print(f"suas duas raizes são x1 = {x1} e x2 = {x2}")

        elif (d == 0):
            print("você tem uma raiz dupla")
            print(f"suas duas raizes são x1 = {x1} e x2 = {x2}")

        elif (d < 0):
            print("você não tem nenhuma raiz real")

    else:
        print("0 não é um número valido para uma equação do 2º grau")


def calculaX():
    a = float(input("dado f(x) = ax²+ bx + c Defina o valor de a: "))
    b = float(input("dado f(x) = ax²+ bx + c Defina o valor de b: "))
    c = float(input("dado f(x) = ax²+ bx + c Defina o valor de c: "))
    x = int(input("Qual o valor de x você quer encontrar: "))

    solve = (a * (x**2)) + (b * x) + c

    print("\n\n")
    print(f"f({x}) = {solve}")


def calculaIntervalo():
    a = float(input("dado f(x) = ax²+ bx + c Defina o valor de a: "))
    b = float(input("dado f(x) = ax²+ bx + c Defina o valor de b: "))
    c = float(input("dado f(x) = ax²+ bx + c Defina o valor de c: "))
    x = int(input("Qual o intervalo [x,y] você quer encontrar, digite o x: "))
    y = int(input("Qual o intervalo [x,y] você quer encontrar, digite o y: "))

    print("\n")
    for k in range(x, y+1, 1):
        solve = (a * (k**2)) + (b * k) + c
        print(f"f({k}) = {solve}")


def barras():
    print("")
    print("Bhaskara 2.0".center(40, '-'))
    print("")


def menu():
    barras()
    print("Selecione uma opção: \n 1 - Encontrar Raiz \n 2 - Substituir um x na lei da função \n"
          + " 3 - Encontrar o intervalo [x,y] para f(x)" + "\n 0 - Sair do programa")
    barras()


def main():

    menu()
    opt = int(input("\nDigite qual opção você deseja: "))

    while opt != 0:
        system('cls')

        if opt == 1:
            print("\n\n")
            EncontraRaiz()
        elif opt == 2:
            print("\n\n")
            calculaX()
        elif opt == 3:
            print("\n\n")
            calculaIntervalo()
        else:
            print("\nOpção invalida, digite novamente!")

        menu()
        opt = int(input("\nDigite qual opção você deseja: "))

    return 0


main()
