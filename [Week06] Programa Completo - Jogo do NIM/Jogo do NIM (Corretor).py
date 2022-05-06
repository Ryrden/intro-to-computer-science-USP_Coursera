def usuario_escolhe_jogada(n, m):
    rmv_piece = m
    rmv_piece = int(input("Quantas peças você vai tirar? "))
    
    while rmv_piece > m or rmv_piece > n or rmv_piece <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        rmv_piece = int(input("Quantas peças você vai tirar? "))

    print("Você tirou", rmv_piece, "peças")
    n -= rmv_piece
    if n == 0:
        print("Fim do jogo! Você ganhou!")
    return rmv_piece


def computador_escolhe_jogada(n, m):
    rmv_piece = m
    if n - rmv_piece == 0:
        return m

    while rmv_piece >= 0:
        winner_strategy = (n-rmv_piece) % (m+1)
        if winner_strategy == 0:
            print("o computador tirou", rmv_piece, "peças")
            return rmv_piece

        rmv_piece -= 1
        if rmv_piece == 0:
            print("o computador tirou", m, "peças")
            return m

    print("o computador tirou", rmv_piece, "peças")
    if n == 0:  # FINAL DO JOGO
        print("Fim do jogo! O computador ganhou!")
    return rmv_piece

def usuario_comeca(n,m):
    while 1:
        User_rmv_piece = usuario_escolhe_jogada(n, m)
        n -= User_rmv_piece
        if n == 0:
            print("Fim do jogo! Você ganhou!")
            return False
        print(f"Agora restam {n} peças no tabuleiro")

        Pc_rmv_piece = computador_escolhe_jogada(n, m)
        n -= Pc_rmv_piece
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            return True

        print(f"Agora restam {n} peças no tabuleiro")

def computador_comeca(n,m):
    while 1:
        Pc_rmv_piece = computador_escolhe_jogada(n, m)
        n -= Pc_rmv_piece
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            return True

        print(f"Agora restam {n} peças no tabuleiro")
        User_rmv_piece = usuario_escolhe_jogada(n, m)
        n -= User_rmv_piece
        if n == 0:
            print("Fim do jogo! Você ganhou!")
            return False

        print(f"Agora restam {n} peças no tabuleiro")
        
def partida(n, m):
    n = 0
    m = 1
    while m >= n:
        print("O limite de peças por jogada não pode ser maior ou igual a quantidade de peças no jogo")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        
    who_starts = n % (m+1)
    if who_starts == 0:
        print("Você começa!")
        return usuario_comeca(n,m)
    else:
        print("Computador começa!")
        return computador_comeca(n,m)


def campeonato(n, m):  # FAZ ISSO OUTRO DIA!!!!!!!!
    PC = User = 0
    games = [partida(n,m) for i in range(3)]

    for Pc_won in games:
        if Pc_won:
            PC += 1
        else:
            User += 1

    return print(f"Placar: Você {User} X {PC} Computador")


def main():
    n = 0  # Peças em Jogo
    m = 0  # Quantidade de peças máxima que é permitido retirar

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    game_type = int(input("2 - para jogar uma partida campeonato "))

    if game_type == 1:
        print("voce escolheu uma partida isolada!")
        partida(n, m)
    if game_type == 2:
        print("voce escolheu um campeonato!")
        campeonato(n, m)

main()
