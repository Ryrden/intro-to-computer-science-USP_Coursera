def eh_hipotenusa(h):
    ca = co = 1

    while h > ca:
        while h > co:
            if h**2 == ca**2 + co**2:
                return True
            co += 1
        co = 1
        ca += 1
    return False


def soma_hipotenusas(x):
    soma = 0
    while x > 1:
        if eh_hipotenusa(x):
            soma += x

        x -= 1
    return soma
