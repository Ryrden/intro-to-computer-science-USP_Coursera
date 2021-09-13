class Triangulo:

    def __init__(self, lado1, lado2, lado3):

        self.a = lado1
        self.b = lado2
        self.c = lado3

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        
        lado1, lado2, lado3 = self.a, self.b, self.c

        if lado1 == lado2 == lado3:
            return 'equilátero'
        
        if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return 'isóceles'
        
        if not lado1 == lado2 == lado3:
            return 'escaleno'

    def retangulo(self):

        a, b, c = self.a, self.b, self.c

        #verificando se é retângulo através do teorema de pitagóras
        if a**2 + b**2 == c**2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        
        a1, b1, c1 = self.a, self.b, self.c 

        a2, b2, c2 = triangulo.a, triangulo.b, triangulo.c

        constante = a2 / a1

        if b2/b1 == constante and c2/c1 == constante:
            return True
        else:
            return False 

if __name__ == "__main__":
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    print(t1.semelhantes(t2))

