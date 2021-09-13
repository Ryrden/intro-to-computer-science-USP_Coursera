import math

a = float(input("dado ax²+ bx + c = 0 Defina o valor de a: "))
b = float(input("dado ax²+ bx + c = 0 Defina o valor de b: "))
c = float(input("dado ax²+ bx + c = 0 Defina o valor de c: "))

delta = (b**2) - (4*a*c) 
if (delta >= 0):
    x1 = -b + math.sqrt(delta)/2*a
    x2 = -b - math.sqrt(delta)/2*a
    if (delta == 0):
        print("a raiz desta equação é", x1)
    else:
        if( x1 <= 0 and x2 >= 0):
            print("as raízes da equação são", x1, "e", x2)
        else:
             print("as raízes da equação são", x2, "e", x1)
else:
    print("esta equação não possui raízes reais")
    