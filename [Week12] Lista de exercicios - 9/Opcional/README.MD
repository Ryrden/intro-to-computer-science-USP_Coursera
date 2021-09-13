## Exercício 1: Triângulos retângulos

Escreva, na classe Triangulo, o método ```retangulo()``` que devolve ```True``` se o triângulo for retângulo, e ```False``` caso contrário.

Exemplos:

```
t = Triangulo(1, 3, 5)
t.retangulo()
```
deve devolver ```False```

```
u = Triangulo(3, 4, 5)
u.retangulo()
```
deve devolver ```True```


## Exercício 2: Triângulos semelhantes

Ainda na classe ```Triangulo```, escreva um método ```semelhantes(triangulo)``` que recebe um objeto do tipo ```Triangulo``` como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver ```True.``` Caso negativo, deve devolver ```False.```

Verifique a semelhança dos triângulos através do comprimento dos lados.

*Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.*

Exemplo:

```
t1 = Triangulo(2, 2, 2)
t2 = Triangulo(4, 4, 4)
t1.semelhantes(t2)
```
deve devolver ```True```