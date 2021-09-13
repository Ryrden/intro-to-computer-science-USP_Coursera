## Exercício 1: Tamanho da matriz

Escreva uma função ```dimensoes(matriz)``` que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

Exemplos:

```
minha_matriz = [[1], [2], [3]]
```
```ruby
dimensoes(minha_matriz)
``` 
deve imprimir 3X1

```
minha_matriz = [[1, 2, 3], [4, 5, 6]]
```
```ruby
dimensoes(minha_matriz)
```
deve imprimir 2X3

## Exercício 2: Soma de matrizes

Escreva a função ```soma_matrizes(m1, m2)``` que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

Exemplos:

```
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
```
```ruby
soma_matrizes(m1, m2)
```
deve devolver [[3, 5, 7], [9, 11, 13]]

```
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
```
```ruby
soma_matrizes(m1, m2)
```
deve devolver ```False```
