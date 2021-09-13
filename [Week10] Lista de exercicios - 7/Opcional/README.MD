## Exercício 1: Imprimindo matrizes

Como proposto na primeira vídeo-aula da semana, escreva uma função ```imprime_matriz(matriz)```, que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. ```Note que NÃO se deve imprimir espaços após o último elemento de cada linha!```

*Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"dessa forma:*

```
>>>print("oi")
oi
>>>
>>>print("oi", end="")
oi>>>

```

Exemplos:

```
minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
1
2
3

```

```
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6

```

## Exercício 2: Matrizes multiplicáveis

Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. Escreva a função ```sao_multiplicaveis(m1, m2)``` que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.

Exemplos:

```
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
```
```ruby
sao_multiplicaveis(m1, m2)
```
deve devolver ```False```

```
m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
```
```ruby
sao_multiplicaveis(m1, m2)
```
deve devolver ```True```