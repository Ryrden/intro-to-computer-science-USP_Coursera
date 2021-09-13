Computador = 0  # Vitorias da máquina
Humano = 0  # Vitorias suas
n = 0  # peças
m = 0  # peças a ser retiradas por jogada


def computador_escolhe_jogada(n, m):
    x = m  # substituto do m para que o próprio não tenha variação

    if n-m != 0:
        if (m+1) % (n-m) == 0 and (n - x) != n < 0:
            n = n - m
        else:
            valid = True  # verificação
            while valid and x >= 1:
                k = (m+1) % (n-x)
                x = x - 1
                if k == 0:  # se n-x for multiplo de m+1
                    n = n - x
                    valid = False
                if x == 0:  # caso o X zere
                    n = n - 1
                    x = 1
                    valid = False
    else:
        x == 1
        n = n - x
    if x == 1:  # para o texto ter "uma"
        print("o computador tirou uma peça")
        if n == 0:  # FINAL DO JOGO
            global Computador
            Computador = Computador + 1
            return print("Fim do jogo! O computador ganhou!")
        print("Agora restam", n, "peças no tabuleiro")
    else:
        print("o computador tirou", x, "peças")
        if n == 0:  # FINAL DO JOGO
            Computador = Computador + 1
            return print("Fim do jogo! O computador ganhou!")
        print("Agora restam", n, "peças no tabuleiro")

    return usuario_escolhe_jogada(n, m)


def usuario_escolhe_jogada(n, m):
    x = m
    valid = True  # verificação
    x = int(input("Quantas peças você vai tirar? "))
    while x > m or valid:
        if x > m or (n - x) == n < 0:
            print("Oops! Jogada inválida! Tente de novo.")
            x = int(input("Quantas peças você vai tirar? "))
        else:
            valid = False

    if x == 1:
        print("Você tirou uma peça.")
        n = n - x
        if n == 0:
            global Humano
            Humano = Humano + 1
            return print("Fim do jogo! Você ganhou!")
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Você tirou", x, "peças")
        n = n - x
        if n == 0:
            Humano = Humano + 1
            return print("Fim do jogo! Você ganhou!")
        print("Agora restam", n, "peças no tabuleiro")

    return computador_escolhe_jogada(n, m)


def partida(n, m):
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (m+1) % n == 0:
        print("Você começa!")
        usuario_escolhe_jogada(n, m)
    else:
        print("Computador começa!")
        computador_escolhe_jogada(n, m)

    return


def campeonato(n, m):
    partida(n, m)
    partida(n, m)
    partida(n, m)

    return print("Você", Humano, "X", Computador, "Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")

print("1 - para jogar uma partida isolada")

tipo_jogo = int(input("2 - para jogar uma partida campeonato "))

if tipo_jogo == 1:
    print("voce escolheu uma partida isolada!")
    partida(n, m)
if tipo_jogo == 2:
    print("voce escolheu um campeonato!")
    campeonato(n, m)
