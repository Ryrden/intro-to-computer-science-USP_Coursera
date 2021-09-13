width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

x = width

while height > 0:
    width = x
    while width > 0:
        print("#", end= "")
        width = width - 1 
    height = height - 1 
    print("")