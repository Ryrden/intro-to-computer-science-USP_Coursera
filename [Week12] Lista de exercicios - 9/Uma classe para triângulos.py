class Triangulo:

    def __init__(self, lado1, lado2, lado3):

        self.a = lado1
        self.b = lado2
        self.c = lado3

    def perimetro(self):
        return self.a + self.b + self.c


# Verificando
if __name__ == "__main__":

    t = Triangulo(1, 1, 1)

    print(t.a)
    print(t.b)
    print(t.c)
    print(t.perimetro)
