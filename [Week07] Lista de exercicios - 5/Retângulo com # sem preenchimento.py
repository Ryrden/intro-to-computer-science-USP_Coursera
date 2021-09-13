width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

x = width
y = height
k = width - 2
kk = k

while height > 0:
    width = x
    while width > 0:
        if height > 1 and height < y:
                kk = k
                print("#", end="")
                while kk > 0:
                    print("", end=" ")
                    kk = kk - 1 
                print("#")
                height = height - 1
        else:    
            print("#", end= "")
            width = width - 1
    height = height - 1 
    print("")
