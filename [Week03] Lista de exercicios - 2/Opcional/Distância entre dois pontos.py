import math

x1 = float(input("Digite o X da sua primeira coordenada: "))
y1 = float(input("Digite o Y da sua primeira coordenada: "))
x2 = float(input("Digite o X da sua segunda coordenada: "))
y2 = float(input("Digite o Y da sua segunda coordenada: "))

Dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if(Dist >= 10):
    print("longe")
else:
    print("perto")
    