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

        
# Verificando 
if __name__ == '__main__':

    t = Triangulo(4, 4, 4)
    print(t.tipo_lado())

    u = Triangulo(3, 4, 5)
    print(u.tipo_lado())

    x = Triangulo(2,3,2)
    print(x.tipo_lado())
            
    
    