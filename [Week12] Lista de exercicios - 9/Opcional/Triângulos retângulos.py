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

# Verificando 
if __name__ == "__main__":
    t = Triangulo(1, 3, 5)
    print(t.retangulo())

    u = Triangulo(3, 4, 5)
    print(u.retangulo())